import openai

def process_image_and_text(text, image_path, api_key):
    """
    텍스트와 이미지를 함께 처리하는 함수.
    """
    openai.api_key = api_key  # API 키 설정

    messages = [
        {"role": "system", "content": "너는 동물건강 진단 시스템이야."},
        {"role": "user", "content": text}
    ]

    try:
        with open(image_path, 'rb') as image:
            response = openai.ChatCompletion.create(
                model="gpt-4-vision",
                messages=messages,
                files=[{
                    "name": "image.jpg",
                    "file": image
                }],
                max_tokens=300
            )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"에러 발생: {e}"

