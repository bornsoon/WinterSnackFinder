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

### 📜 About
<hr>

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

### 📌 담당 역할
<hr>

- **`  군고구마 지도 페이지  `**
  - 군고구마 판매하는 편의점  **주소를 웹 크롤링** 을 통해 수집
  - 주소의 위치를 좌표로 변환해주는 홈페이지를 활용한 좌표 변환  **자동화 처리**
  - 각 구별로 수량에 따라 지도 마크업 아이콘 크기 적용
  - Vercel 배포
 
  ![image](https://github.com/user-attachments/assets/6e84c70a-be34-4b5e-a76c-52732fab5739)

<br><br>

### 📌 상세 구현
<hr>

![image](https://github.com/user-attachments/assets/de5b1b5a-682d-453f-99b7-0c64658fccc1)

<br><br>

### 💬 회고
<hr>

###### *짧은 기간 동안 진행한 미니 프로젝트였지만, 크롤링에 대해 더욱 깊이 이해할 수 있는 기회가 되었다.*
###### *Selenium과 BeautifulSoup의 두 가지 방식으로 크롤링을 진행해서 크롤링 실력이 많이 향상되었다.*
###### *특히, driver 기능을 활용하여 주소의 좌표를 얻어내야 하는 수작업을 자동화로 처리해서 웹 크롤링부터 좌표를 얻는 작업을 한 번에 처리할 수 있었다.*
###### *그리고 배치 처리 중 오류로 인해 작업이 중단되는 문제가 발생했는데, 이를 해결하는 과정에서 예외처리가 얼마나 중요한지 깨달았다.*
