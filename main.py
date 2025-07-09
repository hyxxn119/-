import streamlit as st

model_data = [
    {"name": "ChatGPT", "developer": "OpenAI", "purpose": ["대화", "코딩 보조", "문서 생성", "Q&A", "요약"],
     "experience": ["초보", "일반인", "전문가"], "budget": ["무료", "유료 OK"], "languages": ["한국어", "영어", "다국어"],
     "description": "범용 대화형 AI로 다양한 자연어 처리 작업에 적합합니다."},
    {"name": "GPT-4", "developer": "OpenAI", "purpose": ["고급 대화", "연구", "창의적 글쓰기", "복잡한 문제 해결"],
     "experience": ["일반인", "전문가"], "budget": ["유료 OK"], "languages": ["한국어", "영어", "다국어"],
     "description": "최신 대형 언어 모델, 다양한 고급 작업 지원."},
    {"name": "Claude", "developer": "Anthropic", "purpose": ["문서 요약", "대화", "데이터 분석"],
     "experience": ["일반인", "전문가"], "budget": ["무료", "유료 OK"], "languages": ["영어"],
     "description": "안전성과 신뢰성에 초점을 맞춘 AI."},
    {"name": "Bard", "developer": "Google", "purpose": ["정보 검색", "대화", "콘텐츠 생성"],
     "experience": ["초보", "일반인", "전문가"], "budget": ["무료"], "languages": ["한국어", "영어"],
     "description": "Google 검색과 연계된 AI 대화 서비스."},
    {"name": "Notion AI", "developer": "Notion", "purpose": ["노트 작성", "문서 요약", "정리"],
     "experience": ["초보", "일반인"], "budget": ["유료 OK"], "languages": ["영어", "한국어"],
     "description": "생산성 도구에 최적화된 AI."},
    {"name": "Midjourney", "developer": "Midjourney Inc.", "purpose": ["이미지 생성", "아트워크"],
     "experience": ["초보", "일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "고품질 AI 이미지 생성 플랫폼."},
    {"name": "DALL·E", "developer": "OpenAI", "purpose": ["이미지 생성", "그래픽 디자인"],
     "experience": ["초보", "일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "텍스트 기반 고해상도 이미지 생성."},
    {"name": "Jasper AI", "developer": "Jasper", "purpose": ["마케팅 콘텐츠", "블로그 작성", "광고 문구 생성"],
     "experience": ["초보", "일반인"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "마케팅 콘텐츠 제작에 특화된 AI."},
    {"name": "Writesonic", "developer": "Writesonic Inc.", "purpose": ["광고", "블로그", "글쓰기 보조"],
     "experience": ["초보", "일반인"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "빠르고 쉬운 콘텐츠 생성 AI."},
    {"name": "GitHub Copilot", "developer": "GitHub / OpenAI", "purpose": ["코딩 보조"],
     "experience": ["일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "IDE 통합형 코드 자동 완성 AI."},
    {"name": "Replit Ghostwriter", "developer": "Replit", "purpose": ["코딩 보조", "실시간 코드 작성"],
     "experience": ["초보", "일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "코딩 환경 내 실시간 AI 지원."},
    {"name": "Stable Diffusion", "developer": "Stability AI", "purpose": ["이미지 생성", "아트워크"],
     "experience": ["일반인", "전문가"], "budget": ["무료", "유료 OK"], "languages": ["영어"],
     "description": "오픈소스 AI 이미지 생성 모델."},
    {"name": "HuggingChat", "developer": "Hugging Face", "purpose": ["대화", "연구", "오픈소스 체험"],
     "experience": ["일반인", "전문가"], "budget": ["무료"], "languages": ["영어"],
     "description": "오픈소스 기반 대화형 AI."},
    {"name": "YouChat", "developer": "You.com", "purpose": ["검색", "대화", "정보 탐색"],
     "experience": ["초보", "일반인"], "budget": ["무료"], "languages": ["영어"],
     "description": "검색과 AI 대화 기능 결합."},
    {"name": "OpenAI Whisper", "developer": "OpenAI", "purpose": ["음성 인식", "자동 자막 생성"],
     "experience": ["일반인", "전문가"], "budget": ["무료", "유료 OK"], "languages": ["영어", "한국어", "다국어"],
     "description": "강력한 음성 인식 모델."},
    {"name": "IBM Watson", "developer": "IBM", "purpose": ["비즈니스 AI", "데이터 분석", "대화"],
     "experience": ["일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어", "한국어"],
     "description": "기업용 AI 솔루션."},
    {"name": "Google Vertex AI", "developer": "Google", "purpose": ["머신러닝 모델 개발", "배포"],
     "experience": ["일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "클라우드 기반 ML 플랫폼."},
    {"name": "Amazon SageMaker", "developer": "Amazon", "purpose": ["머신러닝 모델 개발", "배포"],
     "experience": ["일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "AWS 기반 ML 서비스."},
    {"name": "Cohere", "developer": "Cohere", "purpose": ["텍스트 생성", "분석"],
     "experience": ["일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "API 중심 텍스트 생성 서비스."},
    {"name": "AI21 Studio", "developer": "AI21 Labs", "purpose": ["텍스트 생성", "대화"],
     "experience": ["일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "대형 언어 모델 기반 서비스."},
    {"name": "Mistral", "developer": "Mistral AI", "purpose": ["경량 모델", "빠른 응답"],
     "experience": ["일반인", "전문가"], "budget": ["무료"], "languages": ["영어"],
     "description": "빠르고 효율적인 경량 LLM."},
    {"name": "Runway Gen-2", "developer": "Runway", "purpose": ["비디오 생성", "이미지 변환"],
     "experience": ["일반인", "전문가"], "budget": ["유료 OK"], "languages": ["영어"],
     "description": "멀티모달 AI 생성 플랫폼."},
    {"name": "LLaMA 3", "developer": "Meta", "purpose": ["연구", "커스터마이징", "모델 개발"],
     "experience": ["전문가"], "budget": ["무료"], "languages": ["영어"],
     "description": "고성능 오픈소스 대형 언어 모델."},
    {"name": "EleutherAI GPT-NeoX", "developer": "EleutherAI", "purpose": ["오픈소스 연구", "텍스트 생성"],
     "experience": ["전문가"], "budget": ["무료"], "languages": ["영어"],
     "description": "오픈소스 대형 언어 모델."},
    {"name": "DeepL", "developer": "DeepL GmbH", "purpose": ["번역"],
     "experience": ["초보", "일반인", "전문가"], "budget": ["무료", "유료 OK"], "languages": ["다국어"],
     "description": "고품질 자동 번역 서비스."},
    {"name": "Speechmatics", "developer": "Speechmatics", "purpose": ["음성 인식", "자막 생성"],
     "experience": ["일반인", "전문가"], "budget": ["유료 OK"], "languages": ["다국어"],
     "description": "다국어 음성 인식 서비스."},
    {"name": "Synthesia", "developer": "Synthesia", "purpose": ["AI 영상 제작", "가상 아바타"],
     "experience": ["초보", "일반인"], "budget": ["유료 OK"], "languages": ["영어", "한국어"],
     "description": "가상 아바타 기반 영상 생성 플랫폼."},
    {"name": "Runway ML", "developer": "Runway", "purpose": ["이미지/영상 편집", "생성"],
     "experience": ["초보", "일반인", "전문가"], "budget": ["무료", "유료 OK"], "languages": ["영어"],
     "description": "크리에이티브 AI 편집 도구."},
    {"name": "DeepMind Sparrow", "developer": "DeepMind", "purpose": ["안전한 대화", "연구"],
     "experience": ["전문가"], "budget": ["연구 목적"], "languages": ["영어"],
     "description": "안전성 강화된 연구용 대화 AI."},
]

st.set_page_config(page_title="AI 모델 추천기", layout="wide")
st.title("🤖 Toolify 스타일 AI 모델 추천기 (경험 선택지: 초보, 일반인, 전문가)")

st.markdown("30종 이상의 다양한 AI 모델을 참고하여 목적, 경험, 예산, 지원 언어에 맞게 추천합니다!")

with st.form("user_input"):
    st.subheader("📝 당신의 상황을 알려주세요")

    purpose = st.multiselect("✅ 사용 목적을 선택하세요", [
        "대화", "코딩 보조", "문서 생성", "Q&A", "요약", "정보 검색",
        "마케팅", "광고", "이미지 생성", "아트워크", "노트 작성", "정리", "연구", "번역", "음성 인식", "영상 제작"
    ])

    experience = st.radio("🧠 AI 사용 경험은?", ["초보", "일반인", "전문가"])
    budget = st.radio("💰 예산은?", ["무료", "유료 OK"])

    languages = st.multiselect("🗣️ 지원 언어를 선택하세요", [
        "한국어", "영어", "다국어"
    ])

    submitted = st.form_submit_button("🔍 AI 추천받기")

def filter_models(data, purpose, experience, budget, languages):
    results = []
    for model in data:
        if not purpose or not languages:
            continue
        if any(p in model["purpose"] for p in purpose) and \
           experience in model["experience"] and \
           budget in model["budget"] and \
           any(l in model["languages"] for l in languages):
            results.append(model)
    return results

if submitted:
    if not purpose:
        st.warning("❗️ 사용 목적을 최소 하나 이상 선택해주세요.")
    elif not languages:
        st.warning("❗️ 지원 언어를 최소 하나 이상 선택해주세요.")
    else:
        matched = filter_models(model_data, purpose, experience, budget, languages)
        if not matched:
            st.warning("😢 조건에 맞는 모델을 찾을 수 없습니다. 선택지를 넓혀보세요.")
        else:
            st.subheader("📌 추천 결과")
            for model in matched:
                with st.container():
                    st.markdown(f"### 🧠 {model['name']} ({model['developer']})")
                    st.markdown(f"- 🔍 **설명:** {model['description']}")
                    st.markdown(f"- 🎯 **주요 목적:** {', '.join(model['purpose'])}")
                    st.markdown(f"- 🧠 **사용 경험 대상:** {', '.join(model['experience'])}")
                    st.markdown(f"- 💰 **비용:** {', '.join(model['budget'])}")
                    st.markdown(f"- 🗣️ **지원 언어:** {', '.join(model['languages'])}")
                    st.markdown("---")
