<img width="1047" height="420" alt="image" src="https://github.com/user-attachments/assets/a0be4dc8-40f2-4a21-8a79-407582d913e0" />

# 🗺️ 네이버 지도 음식점 크롤링 스크립트

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)

## 🌟 개요

이 스크립트는 **MariaDB**에 저장된 음식점 목록을 활용하여, **네이버 지도**에서 해당 음식점의 상세 정보(리뷰, 평점, 메뉴 등)를 크롤링하고 **MongoDB**에 저장하는 자동화 도구입니다. 병렬 처리를 통해 대량의 데이터를 효율적으로 수집합니다.

---

## ✨ 주요 기능

-   **DB 연동**: MariaDB에서 크롤링할 대상 목록을 가져옵니다.
-   **중복 방지**: MongoDB에 이미 수집된 데이터는 건너뛰어 중복 작업을 방지합니다.
-   **네이버 지도 크롤링**: Selenium을 사용해 브라우저를 자동화하고, 네이버 지도의 상세 페이지에서 데이터를 추출합니다.
-   **주소 교차 검증**: 검색 결과가 여러 개일 경우, 주소 정보를 비교하여 가장 정확한 음식점을 선택합니다.
-   **병렬 처리**: `multiprocessing`을 이용해 여러 작업을 동시에 수행하여 크롤링 속도를 높입니다.
-   **데이터 저장**: 추출된 데이터를 MongoDB에 문서 형태로 저장합니다.

---

## 🛠️ 의존성 설치

스크립트를 실행하기 위해 필요한 라이브러리를 설치합니다.

```bash
pip install pymysql pandas pymongo selenium webdriver-manager tqdm
```
<img width="885" height="37" alt="image" src="https://github.com/user-attachments/assets/4b485926-dea6-4050-9560-9f6797b999d5" />
