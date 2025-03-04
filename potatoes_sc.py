from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv
import re

# 웹드라이버 설정 (Chrome 예시)
driver = webdriver.Chrome()

# 검색 페이지 로드
SEARCH_URL = 'https://gs25.gsretail.com/gscvs/ko/store-services/locations#;'
driver.get(SEARCH_URL)

try:
    # Select box 선택 예시
    # 각 select box의 ID나 name 속성을 사용합니다
    select1 = Select(WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'stb1'))))
    # select2 = Select(driver.find_element(By.ID, 'stb2'))
    select2_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'stb2')))
    select2 = Select(select2_element)

    # 옵션 선택 (index, value, 보이는 텍스트로 선택 가능)
    select1.select_by_value('11')  # value로 선택
    # select2.select_by_index(2)  # 인덱스로 선택 (0부터 시작)
    select1 = Select(WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'stb1'))))
    select1.select_by_value('11')  # 서울 선택
    
    # 두 번째 select box 로딩 대기 및 선택
    select2_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'stb2')))
    select2 = Select(select2_element)

    # for option in select2.options:
    #     print(f"Value: {option.get_attribute('value')}, Text: {option.text}")

    # select2.select_by_value('1123')  # value로 선택
    # select2.select_by_visible_text('동대문구')  # 텍스트로 선택

    option_texts = [option.text for option in select2.options][1:]
    with open('seoul/sweetpotato_seoul.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(option_texts)

    for district in option_texts:
        select2.select_by_visible_text(district)

        try:
            # 방법 1: 클래스로 특정 탭 선택
            # 예: 'CAFE25' 탭 선택
            potatoes_tab =  WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.stsch_nav .nav_tap .potatoes')))
            potatoes_tab.click()

            # # 방법 2: 텍스트로 탭 선택
            # # 특정 텍스트를 포함하는 탭 클릭
            # tab_with_text = driver.find_element(By.XPATH, "//div[@class='stsch_nav']//span[contains(text(), 'CAFE25')]/..")
            # tab_with_text.click()

            # # 방법 3: 여러 탭 순회하며 원하는 탭 선택
            # tabs = driver.find_elements(By.CSS_SELECTOR, '.stsch_nav .nav_tap li a')
            # for tab in tabs:
            #     if tab.text.strip() == 'CAFE25':
            #         tab.click()
            #         break

        except Exception as e:
            print(f"Search or results error: {e}")

        try:
            # 검색 버튼 클릭
            search_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
            search_button.click()

            # 결과 페이지 로딩 대기 (필요한 경우)
            results = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.st_address')))
                

            with open('seoul/sweetpotato_' + district + '.csv', 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['address', 'latitude', 'longitude'])
                for result in results:
                    result_address = result.text
                    # 좌표 추출 (정규표현식 사용)
                    result_coord = re.search(r"'map',\s*(\d+\.\d+),\s*(\d+\.\d+)", result.get_attribute('href'))
                    writer.writerow([result.text, result_coord.group(1), result_coord.group(2)])


        except Exception as e:
            print(f"Search or results error: {e}")

except NoSuchElementException as e:
    print(f"Element not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# 브라우저 종료
driver.quit()