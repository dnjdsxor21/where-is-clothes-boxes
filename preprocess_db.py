import pandas as pd 
import os 
from tqdm.auto import tqdm

####### 도로명주소 위도 경도 값으로 바꿔주기 ########
from naverapi import get_coordinates

# 위도, 경도 반환하는 함수
def geocoding(address):
    client_id = os.environ.get("NAVERAPI_ID")
    client_secret = os.environ.get("NAVERAPI_KEY") 

    geo = get_coordinates(address, client_id, client_secret)
    x_y = geo.split(',')
    x_y = [float(num) for num in x_y]
    return x_y

if __name__=='__main__':
    files = [os.path.join('data', p) for p in sorted(os.listdir('data'), reverse=True)]
    os.makedirs('output', exist_ok=True)
    for file in tqdm(files, total=len(files), desc='file', position=0):
        name, latitude, longitude, address = [], [],[], []
        print(file)
        try:
            df = pd.read_csv(file, engine='python', encoding='CP949')
        except:
            df = pd.read_csv(file, engine='python', encoding='utf-8')


        name = [file.split('/')[-1].split('_')[0]] * len(df)
        if os.path.exists(os.path.join('output', f'{name[0]}.csv')):
            continue
        
        if ('위도' in df.columns) and ('경도' in df.columns):
            latitude = df['위도'].to_list()
            longitude = df['경도'].to_list()
        else:
            for column in df.columns:
                if ('주소' in column) or ('위치' in column) or('설치장소' in column):
                    df.dropna(axis=0, subset=[column], inplace=True)
                    df[column] = df[column].map(lambda x: f'{name[0]} {x.split("(")[0]}' \
                                                if name[0][-4:].strip() not in x else x.split("(")[0])
                    address = df[column].to_list()
                    break
            for addr in tqdm(address, total=len(address), desc='address', leave=False, position=1):
                try:
                    lat,lon = geocoding(addr.strip())
                    if (33<=lat<=43) and (124<=lon<=132):
                        latitude.append(lat)
                        longitude.append(lon)
                except:
                    continue
        if len(latitude)<1:
            print(f"error: {name[0]}")
        else:
            ### save
            final_df = pd.DataFrame({'name':name[:len(latitude)], 'lat':latitude, 'lon':longitude})
            final_df.to_csv(f'output/{name[0]}.csv',index=False, encoding='utf-8')