import openai
from GetData import pet_info

def process_food_rec(text, api_key, pet_id, jwt_token):
    
    pet_name, pet_birth, pet_category, pet_weight, pet_image_url = pet_info(pet_id, jwt_token)

    openai.api_key = api_key

    messages = [
        {"role": "system", "content": "너는 애완동물 먹이 추천 시스템이야."},
        { "role": "user", "content": text 
        +f"{pet_name}은(는) 생년 월일이{pet_birth}이고, 종은 {pet_category}, 몸무게는 {pet_weight}야. 이에 맞춤 음식 또는 사료를 추천해줘."
        +"공백 포함 300자 이내로 답변할 것."
        }
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
