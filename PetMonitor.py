import openai  # OpenAI 패키지 임포트
from GetData import pet_info

def process_pet_monitor(text, api_key, pet_id, jwt_token):
    
    pet_name, pet_birth, pet_category, pet_weight, pet_image_url = pet_info(pet_id, jwt_token)

    openai.api_key = api_key

    try:
        if (pet_image_url != "No Image Available"):
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text":
                            "동물이 건강해 보인다면 \"해당 동물은 건강해보입니다\"라는 응답과 함께 동물이 귀엽습니다 등의 반응을 해줘"
                            +"사진에 동물이 없다면 \"동물 사진이 아닙니다\"라는 응답을 해줘"
                            +f"애완 동물 이름은 {pet_name}이고, 생년 월일은{pet_birth}이고, 종은 {pet_category}, 몸무게는 {pet_weight}야."
                            +"공백 포함 300자 이내로 답변할 것."
                            +text
                            },
                            {
                                "type": "image_url",
                                "image_url": {"url": pet_image_url}  # 이미지 URL 포함
                            }
                        ]
                    }
                ],
                max_tokens=300
            )
        else:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text":
                            "동물이 건강해 보인다면 \"해당 동물은 건강해보입니다\"라는 응답을 해줘"
                            +"동물사진이 있으면 더 정확한 답변을 드릴 수 있습니다. 라는 말을 끝에 붙여줘."
                            +f"애완 동물 이름은 {pet_name}이고, 생년 월일은{pet_birth}이고, 종은 {pet_category}, 몸무게는 {pet_weight}야."
                            +text
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
