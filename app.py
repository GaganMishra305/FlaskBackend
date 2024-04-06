# app.py
from flask import Flask
from flask import Flask, request, jsonify, abort
from werkzeug.exceptions import BadRequest
from flask_cors import CORS
import warnings
warnings.filterwarnings('ignore')

from utils import food_recognition_function, diet_planning_function



app = Flask(__name__)
CORS(app)


@app.route('/',methods=['GET'])
def index():
    return jsonify("welcome to indiet")

@app.route('/recognize_food', methods=['POST'])
def recognize_food():
    if request.method == 'POST':
        image_file = request.files['image']
        data = food_recognition_function(image_file)
        return jsonify(data)

@app.route('/plan_diet', methods=['POST'])
def plan_diet():
    if request.method == 'POST':
        data = request.get_json()
        # print(data)
        weight = data['weight']
        target_calories = data['target_calories']
        diet_plan = diet_planning_function(weight, target_calories)
        return jsonify({'diet_plan': diet_plan})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
