from flask import Flask, render_template, request, jsonify, session
import os
import pandas as pd
import json
from datetime import datetime
from utils.data_processor import process_csv_data
from utils.health_analyzer import analyze_health
from utils.weather_api import get_weather_data

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Ideal values for different crops and growth stages
ideal_values = {
    "Tomato": {
        "pre-fruit": {
            "N": [30, 50], 
            "P": [20, 40], 
            "K": [40, 60], 
            "temperature": [20, 30], 
            "humidity": [60, 80], 
            "pH": [6.0, 6.8], 
            "rainfall": [20, 40]
        },
        "post-fruit": {
            "N": [20, 40], 
            "P": [15, 35], 
            "K": [45, 65], 
            "temperature": [18, 28], 
            "humidity": [65, 85], 
            "pH": [6.2, 7.0], 
            "rainfall": [25, 45]
        }
    },
    "Wheat": {
        "pre-fruit": {
            "N": [40, 60], 
            "P": [30, 50], 
            "K": [20, 40], 
            "temperature": [15, 25], 
            "humidity": [40, 60], 
            "pH": [6.0, 7.5], 
            "rainfall": [15, 30]
        },
        "post-fruit": {
            "N": [30, 50], 
            "P": [25, 45], 
            "K": [25, 45], 
            "temperature": [18, 28], 
            "humidity": [35, 55], 
            "pH": [6.2, 7.8], 
            "rainfall": [10, 25]
        }
    },
    "Rice": {
        "pre-fruit": {
            "N": [50, 70], 
            "P": [25, 45], 
            "K": [30, 50], 
            "temperature": [22, 32], 
            "humidity": [70, 90], 
            "pH": [5.0, 6.5], 
            "rainfall": [40, 60]
        },
        "post-fruit": {
            "N": [40, 60], 
            "P": [20, 40], 
            "K": [35, 55], 
            "temperature": [25, 35], 
            "humidity": [75, 95], 
            "pH": [5.2, 6.8], 
            "rainfall": [45, 65]
        }
    }
}

@app.route('/')
def index():
    # Get list of crops from ideal_values
    crops = list(ideal_values.keys())
    return render_template('index.html', crops=crops)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.csv'):
        # Read the form data
        crop = request.form.get('crop')
        growth_stage = request.form.get('growth_stage')
        location = request.form.get('location')

        # Store selections in session
        session['crop'] = crop
        session['growth_stage'] = growth_stage
        session['location'] = location

        try:
            df = pd.read_csv(file)
            required_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'pH', 'rainfall', 'timestamp']
            for col in required_columns:
                if col not in df.columns:
                    return jsonify({'error': f'Missing required column: {col}'}), 400

            # Process data
            processed_data = process_csv_data(df)

            # ✅ Convert to JSON-safe format
            processed_data_safe = json.loads(pd.DataFrame(processed_data).to_json(orient='records'))

            session['processed_data'] = processed_data_safe

            # Analyze health
            crop_ideal_values = ideal_values.get(crop, {}).get(growth_stage, {})
            health_analysis = analyze_health(processed_data, crop_ideal_values)
            session['health_analysis'] = health_analysis

            # Get weather data
            weather_data = get_weather_data(location)
            session['weather_data'] = weather_data

            return jsonify({'success': True, 'redirect': '/report'})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Only CSV files are allowed'}), 400

@app.route('/report')
def report():
    # Retrieve data from session
    processed_data = session.get('processed_data')
    health_analysis = session.get('health_analysis')
    weather_data = session.get('weather_data')
    crop = session.get('crop')
    growth_stage = session.get('growth_stage')
    location = session.get('location')
    
    if not processed_data or not health_analysis:
        return "No data available. Please upload a CSV file first.", 400
    
    return render_template(
        'report.html',
        crop=crop,
        growth_stage=growth_stage,
        location=location,
        processed_data=json.dumps(processed_data),
        health_analysis=health_analysis,
        weather_data=weather_data
    )

if __name__ == '__main__':
    app.run(debug=True)