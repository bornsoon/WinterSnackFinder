<div align="center">

# 🍠겨울 간식 지도🍠
##### 겨울의 대표 간식인 붕어빵과 군고구마의 위치를 찾기 쉽게 지도로 제공하는 웹 서비스
###### 🌟 <ins>웹 크롤링</ins>을 통해 수집한 서울시 각 구에서 판매되는 겨울 간식의 주소를 지도상에 표시
###### 🌟 각 구별로 겨울 간식의 수량을 아이콘 크기로 직관적으로 표시하고, 클릭 시 상세 위치를 제공
<br>

## 👉👉👉 [ click! 【 🔎겨울간식지도】](https://winter-snack-finder.vercel.app/) 👈👈👈

<img src="https://github.com/user-attachments/assets/4fa57aa9-5aa5-4e51-9b95-455928ec19ee" width=600>

</div>
<br>
<h2>📜 목차</h2>
01. <a href=#1>프로젝트 소개</a><br>
02. <a href=#2>담당 역할</a><br>
03. <a href=#3>상세 구현</a><br>
04. <a href=#4>문제점 및 해결 방안</a><br>
<br><br>

<h2 id=1>📜 About

##### 🗓️ 작업기간 : 2024.12.12 ~ 2024.12.27
##### 👩🏻‍👧‍👦 참여인원 : 2인 (각 지도 별로 담당)
##### 🔧 기술스택

##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📝 언어
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"><br>
##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌱 프레임워크 및 라이브러리
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"/> <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=Vercel&logoColor=white"/> <img src="https://img.shields.io/badge/BeautifulSoup-3776AB?style=for-the-badge&logo=bs4&logoColor=white"> <img src="https://img.shields.io/badge/folium-43B02A?style=for-the-badge&logo=folium&logoColor=white"> <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white">

<br><br>

<h2 id=2>📌 담당 역할</h2>

- **`  군고구마 지도 페이지  `**
  - 군고구마 판매하는 편의점  **주소를 웹 크롤링** 을 통해 수집
  - 주소의 위치를 좌표로 변환해주는 홈페이지를 활용한 좌표 변환  **자동화 처리**
  - 각 구별로 수량에 따라 지도 마크업 아이콘 크기 적용
- **`  Vercel 배포  `**
 
  ![image](https://github.com/user-attachments/assets/6e84c70a-be34-4b5e-a76c-52732fab5739)

<br><br>

<h2 id=3>📌 상세 구현</h2>

![image](https://github.com/user-attachments/assets/de5b1b5a-682d-453f-99b7-0c64658fccc1)

<br><br>

<h2 id=4>🔍 문제점 및 해결 방안💡</h2>

#### 1️⃣ 수집 대상 페이지의 동작 방식 차이
#### &nbsp;🔍 문제점
- ##### 붕어빵과 군고구마 판매 주소를 제공하는 사이트의 동작 방식이 서로 달라 단일 크롤링 방식으로 데이터를 수집할 수 없었다.
#### &nbsp;💡 해결 방안
- ##### 붕어빵 판매 데이터는 `정적 페이지`로 제공되었기 때문에 `BeautifulSoup`을 사용하여 `HTML을 파싱`하여 데이터를 추출할 수 있었다.
- ##### 반면, 군고구마 판매 데이터는 사용자가 `시·구·카테고리 버튼을 선택해야 주소를 조회할 수 있는 동적 페이지`였다. 이에 따라 `Selenium WebDriver`를 활용하여 UI 상호작용을 자동화하는 방식으로 크롤링을 수행했다. 또한, 시·구·카테고리를 선택한 후 데이터가 로딩되는 시간을 고려해서 `적절한 대기 시간을 적용하여 크롤링의 안정성`을 확보했다. 이 방식을 지도 주소 좌표값을 얻을 때도 동일하게 활용하여 원하는 데이터를 수집할 수 있도록 설계했다.
<br>

#### 2️⃣ 지도 주소 좌표 변환 문제
#### &nbsp;🔍 문제점
- ##### Python의 geopy 라이브러리를 활용하여 주소를 좌표값으로 변환하려 했으나, 변환된 좌표값의 소수점 자릿수가 많이 생략되어 실제 주소와 전혀 다른 위치가 반환되는 문제가 발생했다.
#### &nbsp;💡 해결 방안
- ##### 대한민국의 주소를 좌표값으로 변환해주는 외부 사이트를 활용하기로 결정했다.
- ##### 해당 사이트는 `공식 API를 제공하지 않기 때문에 직접 웹 스크래핑을 통해 좌표 변환 기능을 구현`해야 했다.
- ##### `Selenium WebDriver`를 활용하여 <br> 1. 웹페이지를 자동으로 열고 <br> 2. 주소를 입력한 후, <br> 3. 변환된 좌표값을 가져오는 함수를 직접 구현했다.
- ##### 이 함수를 크롤링 과정에서 주소를 수집한 후 호출하여 `주소와 좌표값을 동시에 기록하는 자동화 로직을 설계`함으로써 문제를 해결했다.
<br>

#### 3️⃣ 크롤링 배치 작업 오류
#### &nbsp;🔍 문제점
- ##### 크롤링 대상 데이터 중 `예상치 못한 타입 오류(TypeError) 또는 Null 값`이 포함되어 있을 경우, 스크립트가 중단되는 문제가 발생하여 대량 크롤링 작업이 원활하게 수행되지 않았다.
#### &nbsp;💡 해결 방안
- ##### 데이터 수집 과정에서 발생할 수 있는 예외를 방지하기 위해 `예외 처리 로직을 강화`했다.
- ##### 주요 개선 사항: <br> 1. ` HTML 요소 탐색 실패 처리 `: 크롤링 대상 태그가 존재하지 않는 경우 try-except 블록을 활용하여 기본값을 반환하도록 처리 <br> 2. ` 데이터 타입 변환 오류 방지 `: int(), float() 등의 변환 과정에서 `ValueError 예외`가 발생할 경우, `기본값`을 설정하여 크롤링이 중단되지 않도록 개선 <br> 3. ` Null 값 처리 `: 특정 필드가 존재하지 않을 경우 `기본값(None 또는 "")`을 설정하여 데이터가 누락되지 않도록 설계
- ##### 이를 통해 `배치 작업의 연속성이 보장`되었으며, 대량의 데이터를 안정적으로 크롤링할 수 있었다.

  
<!--
###### *짧은 기간 동안 진행한 미니 프로젝트였지만, 크롤링에 대해 더욱 깊이 이해할 수 있는 기회가 되었다.*
###### *Selenium과 BeautifulSoup의 두 가지 방식으로 크롤링을 진행해서 크롤링 실력이 많이 향상되었다.*
###### *특히, driver 기능을 활용하여 주소의 좌표를 얻어내야 하는 수작업을 자동화로 처리해서 웹 크롤링부터 좌표를 얻는 작업을 한 번에 처리할 수 있었다.*
###### *그리고 배치 처리 중 오류로 인해 작업이 중단되는 문제가 발생했는데, 이를 해결하는 과정에서 예외처리가 얼마나 중요한지 깨달았다.*
-->
