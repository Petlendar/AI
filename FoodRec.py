import openai
from GetData import pet_info

def process_food_rec(text, api_key, pet_id, jwt_token):
    """
    텍스트만 처리하는 함수.
    """
    pet_name, pet_birth, pet_category, pet_weight, pet_image_url = pet_info(pet_id, jwt_token)

    openai.api_key = api_key  # API 키 설정

    messages = [
        {"role": "system", "content": "너는 애완동물 먹이 추천 시스템이야."},
        { "role": "user", "content": text 
        +"애완 동물 관련 질문이 아니라면\"동물 관련 질문이 아닙니다.\"라는 응답만을 해줘(알겠습니다 앞으로 이렇게 응답하겠습니다라는 말 없이)"
        +f"{pet_name}은(는) 생년 월일이{pet_birth}이고, 종은 {pet_category}야. 이에 맞춤 음식 또는 사료를 추천해줘."
        }
    ] # 서버 정보 활용 필요(몸무게, 나이, 종)
    
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
