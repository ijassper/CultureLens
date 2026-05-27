# 문화재 정보를 담고 있는 딕셔너리 - API
culture_db = {
    "다보탑": "신라의 예술미가 돋보이는 탑입니다.",
    "불국사": "통일신라 시대의 대표적인 사찰입니다.",
    "석굴암": "정교하게 설계된 화강암 석굴 사원입니다."
}
# 문화재 설명을 찾아주는 함수
def get_docent_info(name):
    # 입력값으로 백엔드에서 데이터 처리
    info = culture_db

    return info

# 사용자 인터페이스
user_input = input("궁금한 문화재 이름을 입력하세요: ")

# 함수 실행
result = get_docent_info(user_input)
# 출력
print()
