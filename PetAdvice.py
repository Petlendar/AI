import openai
from GetData import pet_info


def process_pet_advice(text, api_key, pet_id, jwt_token):
    
    pet_name, pet_birth, pet_category, pet_weight, pet_image_url = pet_info(pet_id, jwt_token)

    openai.api_key = api_key

    messages = [
        {"role": "system", "content": "너는 반려동물 관련 상담 시스템이야."},
        {"role": "user", "content":
         "애완 동물 관련 질문이 아니라면\"동물 관련 질문이 아닙니다. 동물 관련 질문을 해주세요.\"라는 응답만을 해줘(알겠습니다 앞으로 이렇게 응답하겠습니다라는 말 없이)"
        +f"애완 동물 이름은 {pet_name}이고, 생년 월일은{pet_birth}이고, 종은 {pet_category}, 몸무게는 {pet_weight}야."
        + text}
    ]
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=300
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"에러 발생: {e}"
