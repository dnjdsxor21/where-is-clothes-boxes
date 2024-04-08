
import os
from supabase import create_client, Client
import pandas as pd 
import unicodedata
from collections import defaultdict
import json

url: str = os.environ.get("SUPABASEURL")
key: str = os.environ.get("SUPABASEKEY")
supabase: Client = create_client(url, key)
TABLE_NAME = 'clothes-box'
ROW1 = "name"
ROW2 = "lat"
ROW3 = "lon"


# print(len(response.data))
# for data in response.data:
#     print(data)

def fetch_table(name):
    name = unicodedata.normalize("NFC", name)
    # print(name)
    response = supabase.table(TABLE_NAME).select('*').eq(ROW1, name).execute()
    # print(len(response.data))
    return response.data

def insert_table(name:str, lat:float, lon:float):
    data, count = supabase.table(TABLE_NAME).insert({
        ROW1: name, ROW2:lat, ROW3:lon
        }).execute()
    return data

def update_table(id:int, name=None, lat=None, lon=None):
    data, count = supabase.table(TABLE_NAME).update({
        str(e):e for e in [name, lat,lon] if e is not None
        }).eq('id', id).execute() 
    return data

def delete_table(id:int, name):
    data, count = supabase.table(TABLE_NAME).delete().eq('id', id).execute()
    return data

def upsert_table(id:list, name:list, lat:list, lon:list):
    data, count = supabase.table(TABLE_NAME).upsert(
        [ {'id':a, ROW1:b, ROW2:c, ROW3:d} for (a,b,c,d) in zip(id, name, lat, lon)]
        ).execute()
    return data

if __name__=='__main__':
    files = os.listdir('output')[:]

    ## csv파일 합치기
    df = None 
    for file in files:
        print(file)
        try:
            tmp = pd.read_csv(os.path.join('output', file), engine='python', encoding='utf-8')
            df = pd.concat([df, tmp], axis=0) if df is not None else tmp
        except:
            tmp = pd.read_csv(os.path.join('output', file), engine='python', encoding='CP949')
            df = pd.concat([df, tmp], axis=0) if df is not None else tmp
    df = df.reset_index()
    df[ROW1] = df[ROW1].map(lambda name: unicodedata.normalize('NFC', name))

    df = df[['name', 'lat', 'lon']].dropna(axis=0)
    df.to_csv('db.csv', index=False, encoding='utf-8')
    

    ## meta data 만들기
    metadict = defaultdict(list)
    for n in list(df[ROW1].unique()):
        si, do = n.split()
        metadict[si].append(do)
    json_string = json.dumps(metadict, indent=4, ensure_ascii=False)
    with open('meta.json','w', encoding='utf-8') as f:
        f.write("metaFile = ")
        f.write(json_string)
        

    # supabase 업로드
    upsert_table(
        id=list(df.index+10), name=df['name'].to_list(), lat=df['lat'].to_list(), lon=df['lon'].to_list()
    )
