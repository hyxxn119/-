import streamlit as st

model_data = [
    {"name":"ChatGPT", "developer":"OpenAI", "purpose":["대화","코딩 보조","문서 생성","Q&A","요약","이메일 작성","텍스트 생성"], "experience":["초보","일반인","전문가"], "budget":["무료","유료 OK"], "languages":["한국어","영어","다국어"], "description":"범용 AI 챗봇."},
    {"name":"GPT‑4", "developer":"OpenAI", "purpose":["고급 대화","창의적 글쓰기","복잡한 문제 해결","텍스트 생성"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["한국어","영어","다국어"], "description":"고급 LLM."},
    {"name":"Claude Opus", "developer":"Anthropic", "purpose":["문서 요약","데이터 분석","코딩 보조","요약"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"코딩/분석 강점 LLM."},
    {"name":"Claude Sonnet", "developer":"Anthropic", "purpose":["일반형 대화"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"균형형 Claude 모델."},
    {"name":"Google Gemini 2.5 Pro", "developer":"Google", "purpose":["대화","코딩 보조","정보 검색"], "experience":["초보","일반인","전문가"], "budget":["무료","유료 OK"], "languages":["한국어","영어"], "description":"강력한 멀티모달 AI"},
    {"name":"Grok‑3", "developer":"xAI", "purpose":["대화","수학/과학 추론"], "experience":["일반인","전문가"], "budget":["기업/유료"], "languages":["영어"], "description":"벡터 수학·논리 강점 모델."},
    {"name":"Bard", "developer":"Google", "purpose":["정보 검색","대화","콘텐츠 생성"], "experience":["초보","일반인","전문가"], "budget":["무료"], "languages":["한국어","영어"], "description":"검색 연동 챗봇."},
    {"name":"Perplexity AI", "developer":"Perplexity", "purpose":["정보 검색","QA"], "experience":["초보","일반인"], "budget":["무료"], "languages":["영어"], "description":"검색 기반 답변 제공."},
    {"name":"DeepSeek R1", "developer":"DeepSeek", "purpose":["대화","추론"], "experience":["일반인","전문가"], "budget":["무료"], "languages":["영어"], "description":"비용 효율적인 추론 LLM."},
    {"name":"Qwen 3", "developer":"Alibaba", "purpose":["대화","멀티모달"], "experience":["일반인","전문가"], "budget":["무료"], "languages":["영어","한국어"], "description":"중국 오픈소스 멀티모달 LLM."},
    {"name":"Copilot", "developer":"GitHub/OpenAI", "purpose":["코딩 보조"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"IDE 코드 자동 완성 AI."},
    {"name":"Replit Ghostwriter", "developer":"Replit", "purpose":["코딩 보조"], "experience":["초보","일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"코딩 실시간 지원."},
    {"name":"AlphaEvolve", "developer":"Google DeepMind", "purpose":["코딩 에이전트"], "experience":["전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"고급 코딩 설계 에이전트."},
    {"name":"DALL·E 3", "developer":"OpenAI", "purpose":["이미지 생성"], "experience":["초보","일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"고해상도 이미지 생성."},
    {"name":"Midjourney", "developer":"Midjourney Inc.", "purpose":["이미지 생성","아트워크"], "experience":["초보","일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"예술적 이미지 생성."},
    {"name":"Stable Diffusion", "developer":"Stability AI", "purpose":["이미지 생성"], "experience":["일반인","전문가"], "budget":["무료","유료 OK"], "languages":["영어"], "description":"오픈소스 이미지 생성."},
    {"name":"Runway Gen‑2", "developer":"Runway", "purpose":["비디오 생성"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"텍스트 → 영상 변환."},
    {"name":"Synthesia", "developer":"Synthesia", "purpose":["영상 제작"], "experience":["초보","일반인"], "budget":["유료 OK"], "languages":["한국어","영어"], "description":"가상 아바타 영상 생성."},
    {"name":"ElevenLabs", "developer":"ElevenLabs", "purpose":["음성 합성"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"고품질 음성 합성."},
    {"name":"Whisper", "developer":"OpenAI", "purpose":["음성 인식"], "experience":["일반인","전문가"], "budget":["무료","유료 OK"], "languages":["한국어","영어"], "description":"다국어 음성 인식."},
    {"name":"DeepL", "developer":"DeepL GmbH", "purpose":["번역"], "experience":["초보","일반인","전문가"], "budget":["무료","유료 OK"], "languages":["다국어"], "description":"자연스러운 번역."},
    {"name":"IBM Watson", "developer":"IBM", "purpose":["비즈니스 AI","데이터 분석"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["영어","한국어"], "description":"기업용 AI 플랫폼."},
    {"name":"Amazon SageMaker", "developer":"Amazon", "purpose":["ML 개발"], "experience":["전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"클라우드 ML 서비스."},
    {"name":"Google Vertex AI", "developer":"Google", "purpose":["ML 개발"], "experience":["전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"클라우드 ML 플랫폼."},
    {"name":"Cohere", "developer":"Cohere", "purpose":["텍스트 생성"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"API 중심 LLM."},
    {"name":"Jasper", "developer":"Jasper", "purpose":["마케팅 콘텐츠"], "experience":["초보","일반인"], "budget":["유료 OK"], "languages":["영어"], "description":"SEO 마케팅 특화 AI."},
    {"name":"Writesonic", "developer":"Writesonic", "purpose":["카피라이팅"], "experience":["초보","일반인"], "budget":["유료 OK"], "languages":["영어"], "description":"광고/블로그 생성 AI."},
    {"name":"Canva Magic Studio", "developer":"Canva", "purpose":["그래픽 디자인"], "experience":["초보","일반인"], "budget":["무료","유료 OK"], "languages":["영어"], "description":"디자인 기반 콘텐츠 생성."},
    {"name":"HubSpot Email Writer", "developer":"HubSpot", "purpose":["이메일 작성"], "experience":["초보","일반인"], "budget":["유료 OK"], "languages":["영어"], "description":"마케팅 이메일 자동 작성."},
    {"name":"Gamma", "developer":"Gamma.app", "purpose":["프레젠테이션"], "experience":["초보","일반인"], "budget":["무료","유료 OK"], "languages":["영어"], "description":"자동 프레젠테이션 제작."},
    {"name":"Fathom", "developer":"Fathom", "purpose":["회의 요약"], "experience":["초보","일반인"], "budget":["무료","유료 OK"], "languages":["영어"], "description":"회의 자동 요약."},
    {"name":"NotebookLM", "developer":"Google", "purpose":["문서 리서치"], "experience":["초보","일반인"], "budget":["무료","유료 OK"], "languages":["영어"], "description":"노트 기반 리서치 도구."},
    {"name":"Zapier Agents", "developer":"Zapier", "purpose":["자동화"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"워크플로우 자동화."},
    {"name":"n8n", "developer":"n8n.io", "purpose":["자동화"], "experience":["일반인","전문가"], "budget":["무료","유료 OK"], "languages":["영어"], "description":"커스터마이징 가능한 자동화."},
    {"name":"Poe", "developer":"Quora", "purpose":["챗봇 플랫폼"], "experience":["초보","일반인"], "budget":["무료"], "languages":["영어"], "description":"다중 모델 챗 플랫폼."},
    {"name":"DeepAI", "developer":"DeepAI", "purpose":["이미지 생성"], "experience":["초보","일반인"], "budget":["무료"], "languages":["영어"], "description":"오픈소스 이미지 AI."},
    {"name":"Character.ai", "developer":"Character AI", "purpose":["대화 캐릭터"], "experience":["초보","일반인"], "budget":["무료"], "languages":["영어"], "description":"캐릭터 기반 대화 AI."},
    {"name":"Suno", "developer":"Suno", "purpose":["음악 생성"], "experience":["일반인","전문가"], "budget":["무료","유료 OK"], "languages":["영어"], "description":"AI 음악 생성."},
    {"name":"Murf", "developer":"Murf.ai", "purpose":["음성 합성"], "experience":["일반인","전문가"], "budget":["유료 OK"], "languages":["영어"], "description":"나레이션 품질 TTS."},
    {"name":"CapCut AI", "developer":"Bytedance", "purpose":["영상 편집"], "experience":["초보","일반인"], "budget":["무료","유료 OK"], "languages":["영어"], "description":"모바일 기반 AI 영상 편집."},
    {"name":"Looka", "developer":"Looka", "purpose":["로고 디자인"], "experience":["초보","일반인"], "budget":["유료 OK"], "languages":["영어"], "description":"AI 기반 브랜드 디자인."},
]


st.set_page_config(page_title="AI 모델 추천기", layout="wide")
st.title("🤖 AI 모델 추천기 (50+ 인기 모델)")

st.markdown("목적, 경험, 예산, 언어에 맞춰 대중적인 모델 중 적합한 도구를 추천합니다!")

# 상위-하위 목적 매핑 (상위 목적을 선택해야 하위 목적 선택 가능)
main_categories = {
    "문서 생성": ["요약", "이메일 작성", "블로그", "보고서 작성", "텍스트 생성"],
    "대화": ["일상 대화", "전문가 Q&A", "고급 대화"],
    "코딩 보조": ["자동완성", "디버깅", "코드 리뷰"],
    "이미지 생성": ["아트워크", "로고 디자인", "썸네일 생성"],
    "영상 제작": ["프레젠테이션", "영상 생성", "영상 편집"],
    "음성 관련": ["음성 인식", "음성 합성", "TTS 나레이션"],
    "마케팅": ["카피라이팅", "광고 문구", "SEO 블로그"],
    "자동화": ["워크플로우", "메일 자동화"],
    "기타": ["회의 요약", "음악 생성", "데이터 분석", "리서치"]
}

# 1) 기존 기본 폼
with st.form("user_input_basic"):
    purpose_basic = st.multiselect("✅ 사용 목적 선택 (기본)", [
        "대화", "일상 대화", "고급 대화", "Q&A", "텍스트 생성", "요약", "이메일 작성", "블로그", "문서 생성",
        "코딩 보조", "자동완성", "디버깅", "정보 검색", "마케팅", "광고",
        "이미지 생성", "아트워크", "로고 디자인", "음성 인식", "음성 합성", "TTS 나레이션",
        "번역", "영상 제작", "프레젠테이션", "영상 생성", "영상 편집",
        "자동화", "회의 요약", "음악 생성", "데이터 분석", "리서치"
    ])
    experience_basic = st.radio("🧠 경험 수준 (기본)", ["초보","일반인","전문가"])
    budget_basic = st.radio("💰 예산 (기본)", ["무료","유료 OK"])
    languages_basic = st.multiselect("🗣️ 지원 언어 (기본)", ["한국어","영어","다국어"])
    submit_basic = st.form_submit_button("🔍 추천 받기 (기본)")

# 2) 상위-하위 목적 다이나믹 폼
with st.expander("🧪 고급 선택 (상위-하위 목적 다이나믹)", expanded=False):
    with st.form("user_input_dynamic"):
        main_selected = st.multiselect("📂 상위 목적 선택", list(main_categories.keys()))
        detailed_purpose = []
        for main_cat in main_selected:
            subs = st.multiselect(f"➡️ '{main_cat}'의 세부 목적 선택", main_categories[main_cat], key=main_cat)
            detailed_purpose.extend(subs)
        experience_dynamic = st.radio("🧠 경험 수준 (고급)", ["초보","일반인","전문가"], key="exp_dynamic")
        budget_dynamic = st.radio("💰 예산 (고급)", ["무료","유료 OK"], key="budget_dynamic")
        languages_dynamic = st.multiselect("🗣️ 지원 언어 (고급)", ["한국어","영어","다국어"], key="lang_dynamic")
        submit_dynamic = st.form_submit_button("🔍 추천 받기 (고급)")

def filter_models(data, purposes, experience, budget, languages):
    return [
        m for m in data
        if purposes and languages
        and any(p in m["purpose"] for p in purposes)
        and experience in m["experience"]
        and budget in m["budget"]
        and any(l in m["languages"] for l in languages)
    ]

# 기본 폼 제출 시
if submit_basic:
    if not purpose_basic:
        st.warning("❗️ 사용 목적을 선택해주세요")
    elif not languages_basic:
        st.warning("❗️ 지원 언어를 선택해주세요")
    else:
        matched = filter_models(model_data, purpose_basic, experience_basic, budget_basic, languages_basic)
        if not matched:
            st.warning("😢 조건에 맞는 AI 모델을 찾을 수 없습니다.")
        else:
            st.subheader("📌 기본 선택지 추천 모델")
            for m in matched:
                st.markdown(f"### 🧠 {m['name']} ({m['developer']})")
                st.markdown(f"- {m['description']}")
                st.markdown(f"- 🎯 용도: {', '.join(m['purpose'])}")
                st.markdown(f"- 🧠 경험: {', '.join(m['experience'])}")
                st.markdown(f"- 💰 예산: {', '.join(m['budget'])}")
                st.markdown(f"- 🗣️ 언어: {', '.join(m['languages'])}")
                st.markdown("---")

# 다이나믹 폼 제출 시
if submit_dynamic:
    if not detailed_purpose:
        st.warning("❗️ 세부 목적을 1개 이상 선택해주세요")
    elif not languages_dynamic:
        st.warning("❗️ 지원 언어를 선택해주세요")
    else:
        matched = filter_models(model_data, detailed_purpose, experience_dynamic, budget_dynamic, languages_dynamic)
        if not matched:
            st.warning("😢 조건에 맞는 AI 모델을 찾을 수 없습니다.")
        else:
            st.subheader("📌 고급 선택지 추천 모델")
            for m in matched:
                st.markdown(f"### 🧠 {m['name']} ({m['developer']})")
                st.markdown(f"- {m['description']}")
                st.markdown(f"- 🎯 용도: {', '.join(m['purpose'])}")
                st.markdown(f"- 🧠 경험: {', '.join(m['experience'])}")
                st.markdown(f"- 💰 예산: {', '.join(m['budget'])}")
                st.markdown(f"- 🗣️ 언어: {', '.join(m['languages'])}")
                st.markdown("---")
