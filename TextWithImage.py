import openai
import os

def process_image_and_text(text, image_url, api_key):
    """
    텍스트와 이미지 URL을 함께 처리하는 함수.
    """
    openai.api_key = api_key  # OpenAI API 키 설정

    messages = [
        {"role": "system", "content": "너는 동물건강 진단 시스템이야."},
        {"role": "user", "content": text}
    ]

    if image_url:
        # 이미지 URL을 OpenAI API에 포함
        messages.append({"role": "user", "content": f"이미지 URL: {image_url}"})

    try:
        # OpenAI Chat API 호출
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=messages,
            max_tokens=300
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"에러 발생: {e}"
