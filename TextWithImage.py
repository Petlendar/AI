import openai  # OpenAI 패키지 임포트

def process_image_and_text(text, image_url, api_key):
    """
    텍스트와 이미지 URL을 함께 처리하는 함수.
    """
    openai.api_key = api_key  # OpenAI API 키 설정

    try:
        # OpenAI API 호출
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # 이미지 url을 받아 분석하는 모델
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": text
                         +"동물이 건강해 보인다면 \"해당 동물은 건강해보입니다\"라는 응답을 해줘"
                         +"사진에 동물이 없다면 \"동물사진이 없습니다\"라는 응답을 해줘"},                        
                        {
                            "type": "image_url",
                            "image_url": {"url": image_url}  # 이미지 URL 포함
                        }
                    ]
                }
            ],
            max_tokens=300
        )

        # 응답 메시지 반환
        return response['choices'][0]['message']['content']

    except Exception as e:
        return f"에러 발생: {e}"
