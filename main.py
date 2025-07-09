import streamlit as st

model_data = [
    {
        "name": "ChatGPT",
        "developer": "OpenAI",
        "purpose": ["코딩 보조", "문서 생성", "Q&A"],
        "experience": ["중", "고"],
        "budget": ["무료", "유료 OK"],
        "interface": ["웹 기반", "API 기반"],
        "description": "전천후 텍스트 생성 도구로 코드, 작문, 요약 등 다양한 작업에 적합"
    },
    {
        "name": "Claude",
        "developer": "Anthropic",
        "purpose": ["문서 요약", "대화"],
        "experience": ["중", "고"],
        "budget": ["무료", "유료 OK"],
        "interface": ["웹 기반"],
        "description": "긴 문서 요약에 강점이 있는 자연어 처리 모델"
    },
    {
        "name": "Perplexity AI",
        "developer": "Perplexity",
        "purpose": ["질문 검색", "정보 탐색"],
        "experience": ["초보", "중"],
        "budget": ["무료"],
        "interface": ["웹 기반"],
        "description": "검색과 AI 답변을 결합한 빠른 정보 탐색 도구"
    },
    {
        "name": "Notion AI",
        "developer": "Notion",
        "purpose": ["문서 요약", "정리", "노트 작성"],
        "experience": ["초보", "중"],
        "budget": ["유료 OK"],
        "interface": ["웹 기반", "앱 기반"],
        "description": "Notion 사용자를 위한 문서 작성 및 정리 보조 도구"
    },
    {
        "name": "Copilot",
        "developer": "GitHub",
        "purpose": ["코딩 보조"],
        "experience": ["중", "고"],
        "budget": ["유료 OK"],
        "interface": ["IDE 플러그인"],
        "description": "개발을 위한 실시간 코드 추천 및 자동 완성 도구"
    }
]

st.set_page_config(page_title="AI 모델 추천기", layout="wide")
st.title("🤖 상황 맞춤 AI 모델 추천기")
st.markdown("당신의 목적과 조건에 맞는 AI 도구를 추천해드립니다!")

with st.form("user_input"):
    st.subheader("📝 당신의 상황을 알려주세요")

    purpose = st.multiselect("✅ 사용 목적을 선택하세요", [
        "문서 요약", "코딩 보조", "질문 검색", "정리", "정보 탐색", "대화", "노트 작성", "문서 생성", "Q&A"
    ])

    experience = st.radio("🧠 AI 사용 경험은?", ["초보", "중", "고"])
    budget = st.radio("💰 예산은?", ["무료", "유료 OK"])
    interface = st.multiselect("💻 원하는 인터페이스를 선택하세요", [
        "웹 기반", "앱 기반", "API 기반", "IDE 플러그인"
    ])

    submitted = st.form_submit_button("🔍 AI 추천받기")

def filter_models(data, purpose, experience, budget, interface):
    results = []
    for model in data:
        if not purpose or not interface:
            # 필수 항목 없으면 빈 결과
            continue

        if any(p in model["purpose"] for p in purpose) and \
           experience in model["experience"] and \
           budget in model["budget"]:
            # 인터페이스 조건은 유연하게 처리 (한개라도 겹치면 OK)
            if any(i in model["interface"] for i in interface):
                results.append(model)
    return results

if submitted:
    if not purpose:
        st.warning("❗️ 사용 목적을 최소 하나 이상 선택해주세요.")
    elif not interface:
        st.warning("❗️ 원하는 인터페이스를 최소 하나 이상 선택해주세요.")
    else:
        matched = filter_models(model_data, purpose, experience, budget, interface)

        if not matched:
            st.warning("😢 조건에 맞는 모델을 찾을 수 없습니다. 선택을 더 넓혀보세요.")
        else:
            st.subheader("📌 추천 결과")
            for model in matched:
                with st.container():
                    st.markdown(f"### 🧠 {model['name']} ({model['developer']})")
                    st.markdown(f"- 🔍 **설명:** {model['description']}")
                    st.markdown(f"- 🎯 **주요 목적:** {', '.join(model['purpose'])}")
                    st.markdown(f"- 🧠 **사용 경험 대상:** {', '.join(model['experience'])}")
                    st.markdown(f"- 💰 **비용:** {', '.join(model['budget'])}")
                    st.markdown(f"- 💻 **인터페이스:** {', '.join(model['interface'])}")
                    st.markdown("---")
