from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS 추가
from dotenv import load_dotenv  # .env 파일에서 환경 변수 로드
import os
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
        # 클라이언트로부터 텍스트, 이미지 및 추가 정보 받기
        text = request.form.get('text')  # 텍스트 받기
        pet_name = request.form.get('pet_name')  # 반려동물 이름 받기
        image = request.files.get('image')  # 이미지 받기

        if not text:
            return jsonify({"error": "텍스트가 제공되지 않았습니다."}), 400

        # 이미지가 있는 경우와 없는 경우를 구분하여 처리
        if image:
            # 이미지 파일 처리
            image_path = os.path.join("uploads", image.filename)
            image.save(image_path)

            # 텍스트 + 이미지 처리
            result = process_image_and_text(text, image_path, api_key)  # API 키 전달
        else:
            # 텍스트만 처리
            result = process_text(text, api_key)  # API 키 전달

        # GPT 응답에 반려동물 이름 등 추가 정보를 결합
        additional_text = f"\n추가 정보 - 반려동물 이름: {pet_name}" if pet_name else "\n추가 정보 없음"
        final_response = result + additional_text

        return jsonify({"response": final_response}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
