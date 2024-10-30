from flask import Flask, request, jsonify, render_template
import openai
from FoodRec import process_food_rec
from PetAdvice import process_pet_advice
from PetMonitor import process_pet_monitor
from VaccineInfo import process_vaccine_info

import os
from dotenv import load_dotenv  # .env 파일에서 환경 변수 로드


app = Flask(__name__)

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
api_key = os.getenv("OPENAI_API_KEY")


@app.route('/') #테스트 템플릿 반환
def home():
    return render_template('test.html')

@app.route('/food', methods=['POST'])
def food_recommendation():
    data = request.get_json()
    text = data.get('text', '')
    result = process_food_rec(text, api_key)
    return jsonify({"result": result})

@app.route('/petadvice', methods=['POST'])
def text_analysis():
    data = request.get_json()
    text = data.get('text', '')
    result = process_pet_advice(text, api_key)
    return jsonify({"result": result})

@app.route('/petmonitor', methods=['POST'])
def text_with_image_analysis():
    data = request.get_json()
    text = data.get('text', '')
    image_url = data.get('image_url', '')
    result = process_pet_monitor(text, image_url, api_key)
    return jsonify({"result": result})

@app.route('/vaccine', methods=['POST'])
def vaccine_info():
    data = request.get_json()
    text = data.get('text', '')
    result = process_vaccine_info(text, api_key)
    return jsonify({"result": result})

if __name__ == '__main__':
    # 서버 열기
    app.run(host='0.0.0.0', port=5000)
