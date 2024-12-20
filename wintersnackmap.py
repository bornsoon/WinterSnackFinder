import folium
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from my_location import get_network_location

google_api_key = "AIzaSyANRDxWgZ1YWLhSVKK5tD__RMY2KgmX-ec"
current_lat, current_lng = get_network_location(google_api_key)


seoul_map = folium.Map(location=[37.55, 126.98], tiles='OpenStreetMap', zoom_start=12)
seoul_map2 = folium.Map(location=[37.55, 126.98], tiles='OpenStreetMap', zoom_start=12)


# 사용자 정의 아이콘 생성
def create_bungeo_icon():
    return folium.CustomIcon(
        icon_image='./static/images/bungeoppang3.png',
        icon_size=(65, 65)
    )

# icon_bung = folium.CustomIcon(
#     icon_image='./WintersnackFinder/bungeoppang2.png',  # 아이콘 이미지 경로
#     icon_size=(65, 65)  # 아이콘 크기 (픽셀 단위)
# )


icon_sweetpotato = folium.CustomIcon(
    icon_image='./static/images/sweetpotato2.png',  # 아이콘 이미지 경로
    icon_size=(65, 65)  # 아이콘 크기 (픽셀 단위)
)

# 사용자 정의 아이콘을 가진 마커 추가
# folium.Marker(
#    location=[37.5665, 127.0374],  # 마커 위치
#    popup='붕어빵!',    # 팝업 텍스트
#    icon=create_bungeo_icon()
# ).add_to(seoul_map)

# folium.Marker(
#    location=[37.5669364,127.0671935],  # 마커 위치
#    popup='붕어빵!',    # 팝업 텍스트
#    icon=create_bungeo_icon()
# ).add_to(seoul_map)

#folium.Marker(
#    location=[37.5665, 127.0374],  # 마커 위치
#    popup='군고구마!',    # 팝업 텍스트
#    icon=icon_sweetpotato
#).add_to(seoul_map2)

#seoul_map.save('./templates/seoul3.html')
#seoul_map2.save('./templates/find_sweetpotato.html')


#main-content > div._6vo5t01._6vo5t00._588sy4n8._588sy4nl._588sy4o4._588sy4on._588sy4ou._588sy4p7._588sy4k2._588sy4kf._588sy4ky._588sy4lh._588sy4lo._588sy4m1._588sy4n._588sy462 > div._588sy41z._588sy421._588sy42q._588sy413q._588sy462._588sy4pq._588sy4rb._588sy4ue > div > ul > li:nth-child(1) > a
# --------------------------------------------------------------------------------------------------------------

'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# 붕어빵 검색
data = requests.get('https://www.daangn.com/kr/local-profile/?disableSearch=false&in=%EB%8F%99%EB%8C%80%EB%AC%B8%EA%B5%AC-87&search=%EB%B6%95%EC%96%B4%EB%B9%B5&themeIds=442',headers=headers)

data_address = requests.get('https://www.daangn.com/kr/local-profile/%EB%B6%95%EC%96%B4%EB%B9%B5-rsbw3nmswjv9/?in=%EB%8F%99%EB%8C%80%EB%AC%B8%EA%B5%AC-87',headers=headers)


soup = BeautifulSoup(data.content.decode('utf-8', 'ignore'), 'html.parser')
soup_address = BeautifulSoup(data_address.content.decode('utf-8', 'ignore'), 'html.parser')
#print(soup)

base_url = "https://www.daangn.com"
page_num = 1
bung_address_list = []
while True:
    # li 요소 선택
    selector = f'#main-content > div._6vo5t01._6vo5t00._588sy4n8._588sy4nl._588sy4o4._588sy4on._588sy4ou._588sy4p7._588sy4k2._588sy4kf._588sy4ky._588sy4lh._588sy4lo._588sy4m1._588sy4n._588sy462 > div._588sy41z._588sy421._588sy42q._588sy413q._588sy462._588sy4pq._588sy4rb._588sy4ue > div > ul > li:nth-child({page_num}) > a'
    bung_detail = soup.select_one(selector)
    
    # 더 이상 요소가 없으면 반복 종료
    if not bung_detail:
        break
        
    try:
        detail_url = base_url + bung_detail['href']
        print(f"Processing page {page_num}: {detail_url}")
        
        # 상세 페이지 크롤링
        detail_response = requests.get(detail_url, headers=headers)
        detail_soup = BeautifulSoup(detail_response.content.decode('utf-8', 'ignore'), 'html.parser')
        
        # 상세 페이지에서 주소 추출
        address_selector = '#main-content > div._6vo5t01._6vo5t00._588sy4n8._588sy4nl._588sy4o4._588sy4on._588sy4ou._588sy4p7._588sy4k2._588sy4kf._588sy4ky._588sy4lh._588sy4lo._588sy4m1._588sy4n._588sy462 > article > aside > section > div > ul > li > div > span > button > span'
        bung_address = detail_soup.select_one(address_selector)
        if bung_address:
            print(f"주소: {bung_address.get_text().strip()}")
            bung_address_list.append(bung_address.get_text().strip())
        # 과도한 요청 방지를 위한 대기
        #time.sleep(1)
        
    except Exception as e:
        print(f"Error processing page {page_num}: {str(e)}")
    
    page_num += 1

print("크롤링 완료!")


print(bung_address_list)

df = pd.DataFrame(bung_address_list, columns=['붕어빵 주소'])
df.to_csv('./location_address/bungeoppang_address.csv', index=False, encoding='utf-8-sig')
'''

df_address = pd.read_csv('./location_address/bungeoppang_address_coordinate.csv', encoding='utf-8-sig')
# print(df_address)


# print(df_address.columns)
# print(df_address.dtypes)


# 마커 추가
for idx, row in df_address.iterrows():
    popup_html = f"""
    <div style="font-size: 16px;
                color: black;
                display: flex; 
                align-items: center;
                padding: 10px;
                min_width: fit-content /* 내용에 맞게 최소 너비 설정 */
                white-space: nowrap;     /* 자동 줄바꿈 허용 */
                ">
        <span style="font-weight: bold; margin-left: 8px; margin-right: 8px;">{row['붕어빵 주소']}</span>
    </div>
    """
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=folium.Popup(popup_html, max_width=500),
        icon=create_bungeo_icon()
    ).add_to(seoul_map)


# 지도 저장
# seoul_map.save('./templates/seoul3.html')
# seoul_map.save('./templates/find_bungeoppang.html')








# 첫 번째 페이지에서 상세 페이지 링크 추출
#base_url = "https://www.daangn.com"
#bung_detail = soup.select_one('a.click_search_result_item')
#if bung_detail:
#    detail_url = base_url + bung_detail['href']
    #print(detail_url)
    
    # 상세 페이지 크롤링
    #detail_response = requests.get(detail_url, headers=headers)
    #detail_soup = BeautifulSoup(detail_response.content.decode('utf-8', 'ignore'), 'html.parser')
    #print(detail_soup)
    # 상세 페이지에서 원하는 정보 추출
    #common_tag = '#main-content > div._6vo5t01._6vo5t00._588sy4n8._588sy4nl._588sy4o4._588sy4on._588sy4ou._588sy4p7._588sy4k2._588sy4kf._588sy4ky._588sy4lh._588sy4lo._588sy4m1._588sy4n._588sy462 > article > aside > section > div > ul > li > div > span > button > span'
    #bung_address = detail_soup.select_one(common_tag).get_text().strip()
    #print(bung_address)

#base_url = "https://www.daangn.com" # 기본 URL
#common_tag = '#main-content > div._6vo5t01._6vo5t00._588sy4n8._588sy4nl._588sy4o4._588sy4on._588sy4ou._588sy4p7._588sy4k2._588sy4kf._588sy4ky._588sy4lh._588sy4lo._588sy4m1._588sy4n._588sy462 > div._588sy41z._588sy421._588sy42q._588sy413q._588sy462._588sy4pq._588sy4rb._588sy4ue > div > ul > '
#num = 1
#bung_detail = soup.select_one(common_tag + 'li:nth-child(' + str(num) + ') > a')


# bung_detail = soup.select_one('#main-content > div._6vo5t01._6vo5t00._588sy4n8._588sy4nl._588sy4o4._588sy4on._588sy4ou._588sy4p7._588sy4k2._588sy4kf._588sy4ky._588sy4lh._588sy4lo._588sy4m1._588sy4n._588sy462 > div._588sy41z._588sy421._588sy42q._588sy413q._588sy462._588sy4pq._588sy4rb._588sy4ue > div > ul > li:nth-child(1) > a' )

#bung_address = soup_address.select_one('#main-content > div._6vo5t01._6vo5t00._588sy4n8._588sy4nl._588sy4o4._588sy4on._588sy4ou._588sy4p7._588sy4k2._588sy4kf._588sy4ky._588sy4lh._588sy4lo._588sy4m1._588sy4n._588sy462 > article > aside > section > div > ul > li > div > span > button > span').get_text().strip()

# print(bung_detail)
# print(bung_detail['href'])
# print(bung_address)

#main-content > div._6vo5t01._6vo5t00._588sy4n8._588sy4nl._588sy4o4._588sy4on._588sy4ou._588sy4p7._588sy4k2._588sy4kf._588sy4ky._588sy4lh._588sy4lo._588sy4m1._588sy4n._588sy462 > div._588sy41z._588sy421._588sy42q._588sy413q._588sy462._588sy4pq._588sy4rb._588sy4ue > div > ul > li:nth-child(2) > a

##main-content > div._6vo5t01._6vo5t00._588sy4n8._588sy4nl._588sy4o4._588sy4on._588sy4ou._588sy4p7._588sy4k2._588sy4kf._588sy4ky._588sy4lh._588sy4lo._588sy4m1._588sy4n._588sy462 > div._588sy41z._588sy421._588sy42q._588sy413q._588sy462._588sy4pq._588sy4rb._588sy4ue > div > ul > li:nth-child(43) > a

#title = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a ')