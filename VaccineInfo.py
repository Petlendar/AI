import openai
from GetData import pet_info, vaccine_info

def process_vaccine_info(text, api_key, pet_id, jwt_token):
    
    pet_name, pet_birth, pet_category, pet_weight, pet_image_url = pet_info(pet_id, jwt_token)
    
    try:
        vaccine_name, vaccine_date = vaccine_info(pet_id, jwt_token)
    except Exception as e:
        if "404" in str(e): # 404 반환 시
            vaccine_name = "정보 없음"
            vaccine_date = "정보 없음"
        else:
            return f"에러 발생: {e}"
    
    openai.api_key = api_key

    messages = [
        {"role": "system", "content": "너는 애완동물의 예방접종 정보 제공 시스템이야."},
        {"role": "user", "content": text 
        +"애완 동물 관련 질문이 아니라면\"동물 관련 질문이 아닙니다.\"라는 응답만을 해줘(알겠습니다 앞으로 이렇게 응답하겠습니다라는 말 없이)"
        +f"애완 동물 이름은 {pet_name}이고, 생년 월일은{pet_birth}이고, 종은 {pet_category}, 몸무게는 {pet_weight}야."
        +f"예방접종 맞은 날짜는 {vaccine_date}이고, 백신 이름은 {vaccine_name}이야."
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
