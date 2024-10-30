import requests

# 반려동물 정보 조회 URL
def pet_info(pet_id, jwt_token):
    # 실제 petId 값으로 교체 필요 (프론트에서 받아야함)
    url = f"http://114.70.216.57/pet/api/pet/{pet_id}"


    # 실제 JWT 토큰으로 대체 필요 (프론트에서 받아야함)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }

    # GET
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        
        pet_name = response_data.get("body", {}).get("name") # 반려 동물 이름
        pet_birth = response_data.get("body", {}).get("birth") # 반려 동물 생일
        pet_category = response_data.get("body", {}).get("category") # 반려동물의 종
        pet_weight = response_data.get("body", {}).get("weight") # 몸무게
        pet_image_url = response_data.get("body", {}).get("petImage", {}).get("imageUrl") # 이미지url
        
    else:
        print("요청 실패:", response.status_code)
