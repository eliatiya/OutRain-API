from flask import Blueprint, request, jsonify
from .weather_service import get_current_weather, get_city_weather
from .drive_service import save_drive_data, get_drive_data
import json
import os

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/checkCurrentWeather', methods=['GET'])
def check_current_weather():
    try:
        data = get_current_weather()
        return jsonify(data)
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@api_blueprint.route('/checkCityWeather', methods=['GET'])
def check_city_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"message": "City parameter is required"}), 400
    try:
        data = get_city_weather(city)
        return jsonify(data)
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@api_blueprint.route('/driveStatus', methods=['POST'])
def post_drive_status():
    try:
        drive_data = request.get_json()
        save_drive_data(drive_data)
        return jsonify({"message": "success"})
    except Exception as e:
        return jsonify({"message": f"failure: {str(e)}"}), 500

@api_blueprint.route('/driveStatus', methods=['GET'])
def get_drive_status():
    status = request.args.get('status')
    if not status:
        return jsonify({"message": "Status parameter is required"}), 400
    try:
        result = get_drive_data(status)
        return json.dumps(result, indent=4)
    except Exception as e:
        return jsonify({"message": str(e)}), 500
