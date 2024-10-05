import openai

def process_text(text, api_key):
    """
    텍스트만 처리하는 함수.
    """
    openai.api_key = api_key  # API 키 설정

    messages = [
        {"role": "system", "content": "너는 동물건강 진단 시스템이야."},
        {"role": "user", "content": text}
    ]
    
    try:
        # 새로운 방식으로 ChatCompletion 호출
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=300
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"에러 발생: {e}"
