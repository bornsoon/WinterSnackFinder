import csv
import folium
import json
import requests
from bs4 import BeautifulSoup
from geo import find_location

seoul_map = folium.Map(location=[37.55, 126.98], tiles='OpenStreetMap', zoom_start=12)

bungeoppang_code = {}

with open('seoul/bungeoppang_seoul.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for i in csv_reader:
        bungeoppang_code.update(i)

for district, code in bungeoppang_code.items():
    print(district, code)
    # 붕어빵 검색
    html = requests.get(f'https://www.daangn.com/kr/local-profile/?disableSearch=false&in={code}&themeIds=442')
    soup = BeautifulSoup(html.content.decode('utf-8', 'ignore'), 'html.parser')

    # JSON-LD 스크립트 태그 추출
    script = soup.find('script', {'type': 'application/ld+json'})

    if script:
        # JSON-LD 데이터를 파싱
        json_data = json.loads(script.string)
        
        # "address" 필드에서 필요한 정보 추출
        item_list = json_data['itemListElement']

        with open('seoul/bungeoppang_' + district + '.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['address', 'latitude', 'longitude'])
            address_list = set()

            for item in item_list:
                try:
                    address = item['item']['address']['streetAddress']
                except KeyError:
                    continue
                if address:
                    address_list.add(address)

            # print(len(address_list)) # 92
            for ad in address_list:
                lat, lng = find_location(ad)
                if lat and lng:
                    writer.writerow([ad, lat, lng])

    else:
        print("JSON-LD 스크립트를 찾을 수 없습니다.")