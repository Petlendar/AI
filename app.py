from flask import Flask, request, jsonify
import openai
from FoodRec import process_food_rec
from PetAdvice import process_pet_advice
from PetMonitor import process_pet_monitor
from VaccineInfo import process_vaccine_info
from GetData import pet_info, vaccine_info
from GetText import extract_text


import os
from dotenv import load_dotenv  # .env 파일에서 환경 변수 로드

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

@app.route('/food', methods=['GET'])
def food_recommendation():
    try:
        data = request.get_json()
        
        extracted_data = extract_text(data)
        if isinstance(extracted_data, tuple):
            text, jwt_token, pet_id = extracted_data
        else:
            return extracted_data # 예외 처리

        result = process_food_rec(text, api_key, pet_id, jwt_token)
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"result": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/petadvice', methods=['GET'])
def pet_advisor():
    try:
        data = request.get_json()
        
        extracted_data = extract_text(data)
        if isinstance(extracted_data, tuple):
            text, jwt_token, pet_id = extracted_data
        else:
            return extracted_data

        result = process_pet_advice(text, api_key, pet_id, jwt_token)
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"result": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/petmonitor', methods=['GET'])
def pet_monotoring():
    try:
        data = request.get_json()
        
        extracted_data = extract_text(data)
        if isinstance(extracted_data, tuple):
            text, jwt_token, pet_id = extracted_data
        else:
            return extracted_data

        result = process_pet_monitor(text, api_key, pet_id, jwt_token)
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"result": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/vaccine', methods=['GET'])
def vaccine_information():
    try:
        data = request.get_json()
        
        extracted_data = extract_text(data)
        if isinstance(extracted_data, tuple):
            text, jwt_token, pet_id = extracted_data
        else:
            return extracted_data

        result = process_vaccine_info(text, api_key, pet_id, jwt_token)
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"result": f"An unexpected error occurred: {str(e)}"}), 500
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
