import streamlit as st

# 추천 로직 함수
def recommend_model(purpose, experience, budget, interface):
    if purpose == "문서 요약" and interface == "웹 기반":
        return "Notion AI"
    elif purpose == "코딩 보조" and experience in ["중", "고"]:
        return "ChatGPT (Pro or Plus)"
    elif purpose == "질문 검색" and budget == "무료":
        return "Perplexity AI"
    elif purpose == "업무 자동화" and experience == "초보":
        return "ChatGPT 또는 Notion AI"
    else:
        return "Claude 또는 기타 LLM 기반 도구"

# 스트림릿 설정
st.set_page_config(page_title="AI 모델 추천기", layout="centered")

st.title("🧠 나에게 딱 맞는 AI 추천기")
st.markdown("간단한 선택만으로 당신에게 적합한 인공지능 도구를 추천해드립니다!")

with st.form("user_input"):
    st.subheader("1️⃣ 당신의 상황을 알려주세요")

    purpose = st.selectbox("사용 목적은 무엇인가요?", [
        "문서 요약", "코딩 보조", "질문 검색", "업무 자동화", "기타"
    ])

    experience = st.selectbox("AI 사용 경험은 어느 정도인가요?", [
        "초보", "중", "고"
    ])

    budget = st.radio("예산은 어느 정도인가요?", ["무료", "유료 OK"])

    interface = st.selectbox("어떤 방식이 더 편한가요?", [
        "웹 기반", "앱 기반", "API 기반"
    ])

    submitted = st.form_submit_button("AI 추천받기!")

# 결과 출력
if submitted:
    result = recommend_model(purpose, experience, budget, interface)
    st.success(f"✅ 추천 모델: **{result}**")
    st.markdown(f"이유: 당신의 상황({purpose}, {experience}, {budget}, {interface})에 적합한 선택입니다.")

    st.markdown("---")
    st.subheader("ℹ️ 자주 추천되는 모델 설명")
    with st.expander("설명 펼치기"):
        st.markdown("""
        - **ChatGPT**: 전천후 텍스트 생성 도구, 코드/문서/글쓰기 모두 가능  
        - **Notion AI**: 문서 기반 AI, 노션 사용자에게 최적  
        - **Perplexity AI**: 실시간 검색 기반, 정보 탐색에 유리  
        - **Claude**: 장문 요약 및 자연스러운 대화에 강점  
        """)
