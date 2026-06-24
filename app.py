import streamlit as st
import json
import random

# 1. JSON 파일 불러오기
@st.cache_data # 데이터를 캐싱하여 앱 속도 높이기
def load_data():
    with open('response_1781098357586.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['response']['body']['items']['item']

items = load_data()
# 문화재 이름(title)을 키로, 상세설명(description)을 값으로 딕셔너리 구축
culture_db = {item['id']: item for item in items}

# 2. UI 구성
st.title("🏛️ AI 문화재 도슨트")
st.write("우리 박물관의 보물을 검색하고 AI의 설명을 들어보세요!")

# 3. 검색창 (st.selectbox 사용)
options = {item['title'] + " (" + item['id'][-5:] + ")": item['id'] for item in items}
selected_label = st.selectbox("문화재 선택:", list(options.keys()))
selected_id = options[selected_label]
item = culture_db[selected_id]

# 4. 결과 출력
if selected:
    st.subheader(f"🔍 {selected}")
    st.success(culture_db[selected])
    
    # 5. 추천 기능
    recommend_list = [key for key in culture_db.keys() if key != selected]
    if recommend_list:
        rec = random.choice(recommend_list)
        st.write("---")
        st.write(f"💡 이번엔 **{rec}**은 어떠신가요?")

# 6. (참고) 데이터 전체 목록 확인 (사이드바)
if st.sidebar.checkbox("전체 데이터 목록 보기"):
    st.sidebar.write(culture_db)
