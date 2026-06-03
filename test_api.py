import streamlit as st
from streamlit_searchbox import st_searchbox
import random
import requests

service_key = st.secrets["SERVICE_KEY"]
search_name = "백제"

url = f"https://api.kcisa.kr/openapi/service/rest/meta/MPKreli?serviceKey={service_key}&numOfRows=10&pageNo=1"

response = requests.get(url, timeout=5)

if response.status_code == 200:
  st.write("데이터 호출 성공")
  st.write(response.text)
else:
  st.write(f"호출 오류: {response.status_code}")

# 문화재 정보를 담고 있는 딕셔너리 - API
culture_db = {
    "다보탑": "신라의 예술미가 돋보이는 탑입니다.",
    "불국사": "통일신라 시대의 대표적인 사찰입니다.",
    "석굴암": "정교하게 설계된 화강암 석굴 사원입니다."
}

# 문화재 설명을 찾아주는 함수
def get_docent_info(name):
    # 입력값으로 백엔드에서 데이터 처리
    return culture_db.get(name)

#받침의 여부 판별
def has_batchim(word):
    last = word[-1]
    return (ord(last) - ord("가")) % 28 != 0

#자동완성 함수
def search_culture(searchterm):
    if not searchterm:
        return []
    return [key for key in culture_db.keys() if searchterm in key]

#검색창
selected = st_searchbox(search_function=search_culture, label="궁금한 문화재 이름을 입력하세요: ")


#문화재 선택 시
if selected:
    result = get_docent_info(selected)
    if result:
        st.write(result)
        recommend_list = [key for key in culture_db.keys() if key != selected]

        random_recommend = random.choice(recommend_list)
        
        if has_batchim(random_recommend):
            particle = "은"
        else:
            particle = "는"
        st.write(f"이번엔 {random_recommend}{particle} 어떠신가요?")
