from folium.plugins.locate_control import LocateControl
import csv
import folium
import folium.plugins

map_center = [37.55, 126.98] 

# locate control 아이콘 설정
locate_control = LocateControl(
        position = 'bottomleft',
        strings = {'title': "내 위치 찾기"},
        locateOptions = {
            'enableHighAccuracy' :  True,
            'maxZoom' : 16
        },
        # icon = 'custom-locate-icon',  # 커스텀 아이콘 클래스
        # iconLoading = 'custom-locate-icon',  # 로딩 중 아이콘
        default_css = 'static/css/wintersnackFinder.css',
        iconElementTag = 'span',
        showCompass = True,
        showPopup = False,  # 팝업 비활성화
        flyTo = True,       # 부드러운 이동
        cacheLocation = True
    )

def spot_csv_reader(category):
    spot_dict = {}

    with open('seoul/seoul.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for i in next(csv_reader):
            spot_dict[i] = []

    for district in spot_dict.keys():
        with open('seoul/'+category+'_'+district+'.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            temp = []

            for l in csv_reader:
                if l['latitude'] and l['longitude']:
                    if len(l['address'].split(',')) > 1:
                        ad = l['address'].split(',')[0]
                    else:
                        ad = l['address']
                    row = {'address': ad, 'latitude': float(l['latitude']), 'longitude': float(l['longitude'])}
                    temp.append(row)

            spot_dict[district] = temp
    return spot_dict


def district_marker(category):
    mymap = folium.Map(location=map_center, zoom_start=12)
    
    spot_dict = spot_csv_reader(category)

    for district, locs in spot_dict.items():
        latitudes = [loc['latitude'] for loc in locs]
        longitudes = [loc['longitude'] for loc in locs]
        avg_lat = sum(latitudes) / len(latitudes)
        avg_lng = sum(longitudes) / len(longitudes)

        popup_html = f"""
            <a href="/{category}/{district}"> [click]
                <div style="font-size: 16px; color: black;">
                    <strong>{district} : {len(locs)}곳</strong>
                </div>
            </a>
            """
        folium.Marker(
                location = [avg_lat, avg_lng],
                popup = folium.Popup(popup_html, max_width=300),
                icon = folium.CustomIcon('static/images/'+category+'3.png', icon_size=(1.4 * len(locs), 1.4 * len(locs)))
            ).add_to(mymap)

    locate_control.add_to(mymap)

    # HTML 저장
    map_html = mymap._repr_html_()

    return map_html


def detail_marker(category, district):
    spot_dict = spot_csv_reader(category)

    latitudes = [loc['latitude'] for loc in spot_dict[district]]
    longitudes = [loc['longitude'] for loc in spot_dict[district]]
    avg_lat = sum(latitudes) / len(latitudes)
    avg_lng = sum(longitudes) / len(longitudes)

    map_center = [avg_lat, avg_lng] 

    mymap = folium.Map(location=map_center, zoom_start=14)
        
    # 마커 추가
    for spot in spot_dict[district]: 
        popup_html = f"""
            <div style="font-size: 16px; color: black;">
                <strong>{spot['address']}</strong>
            </div>
            """
        folium.Marker(
            location = [spot['latitude'], spot['longitude']],
            popup = folium.Popup(popup_html, max_width=300),
            icon = folium.CustomIcon('static/images/'+category+'3.png', icon_size=(50, 50))
        ).add_to(mymap)


    locate_control.add_to(mymap)

    # HTML 저장
    map_html = mymap._repr_html_()

    return map_html