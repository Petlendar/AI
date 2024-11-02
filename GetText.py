from flask import jsonify, request

def extract_text(data):
    if not data:
        return jsonify({"result": "No JSON data provided"}), 400
    
    body = data.get('body')
    if not body:
        return jsonify({"result": "'body' field is missing in the JSON data"}), 400

    text = body.get('text')
    if text is None:
        return jsonify({"result": "'text' field is missing in 'body'"}), 400

    authorization = request.headers.get("Authorization")
    if authorization is None:
        return jsonify({"result": "'Authorization' field is missing in 'body'"}), 400
    if not authorization.startswith("Bearer "):
        return jsonify({"result": "'Authorization' field is incorrectly formatted"}), 400
    jwt_token = authorization.split(" ")[1]

    pet_id = body.get("petId")
    if pet_id is None:
        return jsonify({"result": "'petId' field is missing in 'body'"}), 400

    return text, jwt_token, pet_id