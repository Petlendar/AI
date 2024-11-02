import requests

def pet_info(petId, jwt_token):
    url = f"http://114.70.216.57/pet/api/pet/{petId}"


    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        
        pet_name = response_data.get("body", {}).get("name") # 반려 동물 이름
        pet_birth = response_data.get("body", {}).get("birth") # 반려 동물 생일
        pet_category = response_data.get("body", {}).get("category") # 반려동물의 종
        pet_weight = response_data.get("body", {}).get("weight") # 몸무게
        
        try:
            pet_image_url = response_data.get("body", {}).get("petImage", {}).get("imageUrl")
            
        except AttributeError:
            pet_image_url = "No Image Available"

        return pet_name, pet_birth, pet_category, pet_weight, pet_image_url

    else:
        print("요청 실패:", response.status_code)
        return None

def vaccine_info(petId, jwt_token):
    url = f"http://114.70.216.57/pet/api/vaccination/{petId}"


    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        
        try:
            vaccine_name = response_data.get("body", {}).get("type") # 백신 이름
            vaccine_date = response_data.get("body", {}).get("date") # 접종 날짜
        except AttributeError:
                vaccine_name = "No Vaccine Information"
                vaccine_date = "No Vaccine Information"

        return vaccine_name, vaccine_date

    else:
        print("요청 실패:", response.status_code)
        return None
