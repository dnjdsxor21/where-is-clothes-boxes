import requests
import os 

def get_coordinates(address, client_id, client_secret):
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret
    }
    params = {"query": address}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['addresses']:
            latitude = float(data['addresses'][0]['y'])
            longitude = float(data['addresses'][0]['x'])
            return f"{latitude:.7f},{longitude:.7f}"
        else:
            return "0.00,0.00"
    else:
        print(f"오류 발생 - 상태 코드: {response.status_code}, 응답: {response.text}")
        return "0.00,0.00"

def process_addresses(input_file, output_file, client_id, client_secret):
    with open(input_file, 'r', encoding='utf-8') as file:
        addresses = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for address in addresses:
            address = address.strip()
            if address:
                coordinates = get_coordinates(address, client_id, client_secret)
                print(coordinates)
                file.write(f"{coordinates}\n")

if __name__=="__main__":
    # 사용 예시
    client_id = os.environ.get("NAVERAPI_ID")
    client_secret = os.environ.get("NAVERAPI_KEY") 
    process_addresses('./geocoding/input.txt', 'output.txt', client_id, client_secret)