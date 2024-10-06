import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS 추가
from dotenv import load_dotenv  # .env 파일에서 환경 변수 로드
from OnlyText import process_text  # 텍스트만 처리하는 함수
from TextWithImage import process_image_and_text  # 텍스트 + 이미지 처리 함수

# Flask 앱 생성
app = Flask(__name__)
CORS(app)  # CORS 허용

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return "Flask 서버가 실행 중입니다."

@app.route('/process', methods=['POST'])
def process_request():
    """
    텍스트와 이미지를 처리하고, 추가 정보를 응답에 포함.
    """
    try:
        # JSON 데이터를 받기
        data = request.get_json()  # JSON 형식으로 데이터를 받음
        text = data.get('text')  # 텍스트 받기
        pet_name = data.get('pet_name')  # 반려동물 이름 받기
        image_url = data.get('image_url')  # 이미지 URL 받기

        if not text:
            return jsonify({"error": "텍스트가 제공되지 않았습니다."}), 400

        # 이미지가 있는 경우와 없는 경우를 구분하여 처리
        if image_url:
            # 텍스트 + 이미지 처리
            result = process_image_and_text(text, image_url, api_key)  # API 키 전달
        else:
            # 텍스트만 처리
            result = process_text(text, api_key)  # API 키 전달

        # GPT 응답에 반려동물 이름 등 추가 정보를 결합
        additional_text = f"{pet_name}" if pet_name else "이름 없음"
        final_response = additional_text + "의 진단 결과: " + result

        return jsonify({"response": final_response}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)