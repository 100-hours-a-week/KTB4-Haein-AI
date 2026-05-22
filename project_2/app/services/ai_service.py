# ollama 호출 코드를 API 라우터에서 분리
# router/ai.py : API 주소만 담당 
# services/ai_service.py : 실제 AI 호출 담당
from ollama import chat

# 텍스트를 받아 요약 결과 문자열을 반환하는 함수 
def summarize_text(text: str) -> str:
    prompt = f"""
다음 커뮤니티 내용을 한국어로 200자 이내로 요약해줘.

{text}
"""

    response = chat(
        model="gemma3",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.message.content