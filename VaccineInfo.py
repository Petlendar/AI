import openai
from GetData import pet_info, vaccine_info

def process_vaccine_info(text, api_key, pet_id, jwt_token):
    
    pet_name, pet_birth, pet_category, pet_weight, pet_image_url = pet_info(pet_id, jwt_token)
    

    vaccine_name, vaccine_date = vaccine_info(pet_id, jwt_token)

    openai.api_key = api_key
    try:
        if vaccine_name != "No Vaccine Information":
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages = [
                    {
                        "role": "system", 
                        "content": "너는 애완동물의 예방접종 정보 제공 시스템이야."},
                    {
                        "role": "user",
                        "content":
                    f"애완 동물 이름은 {pet_name}이고, 생년 월일은{pet_birth}이고, 종은 {pet_category}, 몸무게는 {pet_weight}야."
                    +f"그리고 {vaccine_name}를 접종했고, 예방접종 맞은 날짜는 {vaccine_date}"
                    +"공백 포함 300자 이내로 답변할 것."
                    + text
                    }
                ],
                max_tokens=300
                )
        else:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages = [
                    {"role": "system", "content": "너는 애완동물의 예방접종 정보 제공 시스템이야."},
                    {"role": "user", "content":
                    f"애완 동물 이름은 {pet_name}이고, 생년 월일은{pet_birth}이고, 종은 {pet_category}, 몸무게는 {pet_weight}야."
                    +f"\"해당 애완 동물의 예방 접종 관련 정보가 없습니다.\"라는 말을 응답의 시작에 붙여줘."
                    +"공백 포함 300자 이내로 답변할 것."
                    + text
                    }
                ],
                max_tokens=300
            )
        return response['choices'][0]['message']['content']

    except Exception as e:
        return f"에러 발생: {e}"
