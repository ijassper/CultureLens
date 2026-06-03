import streamlit as st
from streamlit_searchbox import st_searchbox
import random

# 1. 문화재 정보를 담고 있는 데이터베이스
culture_db = {
    "다보탑": "신라의 예술미가 돋보이는 탑입니다.",
    "불국사": "통일신라 시대의 대표적인 사찰입니다.",
    "석굴암": "정교하게 설계된 화강암 석굴 사원입니다.",
    "첨성대": "동양에서 가장 오래된 천문 관측대입니다."
}

# 2. 문화재 설명을 찾아주는 함수
def get_docent_info(name):
    return culture_db.get(name)

# 3. 받침 여부 판별 (조사 처리용)
def has_batchim(word):
    if not word: return False
    last_char = word[-1]
    return (ord(last_char) - ord("가")) % 28 != 0

# 4. 검색창 자동완성 함수
def search_culture(searchterm):
    if not searchterm:
        return []
    # 검색어를 포함하는 모든 키를 찾음
    return [key for key in culture_db.keys() if searchterm in key]

# --- UI 시작 ---
st.title("🏛️ AI 문화재 도슨트")

# 검색창 구현 (오타 수정: search_function)
selected = st_searchbox(search_function=search_culture, label="궁금한 문화재 이름을 입력하세요.")

# 문화재 선택 시 로직
if selected:
    result = get_docent_info(selected)
    if result:
        st.subheader(f"🔍 {selected}")
        st.info(result)
        
        # 추천 로직 (데이터가 충분할 때만 실행)
        recommend_list = [key for key in culture_db.keys() if key != selected]
        
        if recommend_list:
            random_recommend = random.choice(recommend_list)
            particle = "은" if has_batchim(random_recommend) else "는"
            st.write(f"---")
            st.write(f"💡 이번엔 {random_recommend}{particle} 어떠신가요?")
