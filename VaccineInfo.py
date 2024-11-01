import openai
from GetData import pet_info, vaccine_info

def process_vaccine_info(text, api_key, pet_id, jwt_token):
    
    pet_name, pet_birth, pet_category, pet_weight, pet_image_url = pet_info(pet_id, jwt_token)
    

    vaccine_data = vaccine_info(pet_id, jwt_token)
    if vaccine_data is None:
        vaccine_name = "No Vaccine Information"
        vaccine_date = "No Vaccine Information"
    else:
        vaccine_name, vaccine_date = vaccine_data
    
    openai.api_key = api_key
    if vaccine_name != "No Vaccine Information":
        messages = [
            {"role": "system", "content": "너는 애완동물의 예방접종 정보 제공 시스템이야."},
            {"role": "user", "content": text 
            +"애완 동물 관련 질문이 아니라면\"동물 관련 질문이 아닙니다.\"라는 응답만을 해줘(알겠습니다 앞으로 이렇게 응답하겠습니다라는 말 없이)"
            +f"애완 동물 이름은 {pet_name}이고, 생년 월일은{pet_birth}이고, 종은 {pet_category}, 몸무게는 {pet_weight}야."
            +f"예방접종 맞은 날짜는 {vaccine_date}이고, 백신 이름은 {vaccine_name}이야."
            }
        ]
    else:
        messages = [
            {"role": "system", "content": "너는 애완동물의 예방접종 정보 제공 시스템이야."},
            {"role": "user", "content": text 
            +"애완 동물 관련 질문이 아니라면\"동물 관련 질문이 아닙니다.\"라는 응답만을 해줘(알겠습니다 앞으로 이렇게 응답하겠습니다라는 말 없이)"
            +f"애완 동물 이름은 {pet_name}이고, 생년 월일은{pet_birth}이고, 종은 {pet_category}, 몸무게는 {pet_weight}야."
            +f"\"해당 애완 동물의 예방 접종 관련 정보가 없습니다.\"라는 말을 응답의 끝에 붙여줘."
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
