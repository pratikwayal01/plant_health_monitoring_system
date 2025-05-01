from flask import Flask, flash, render_template, request, jsonify, session, redirect, url_for
import os
import pandas as pd
import json
from datetime import datetime
from utils.data_processor import process_csv_data
from utils.health_analyzer import analyze_health
from utils.weather_api import get_weather_data
from utils.crop_manager import add_new_crop, get_crop_list, get_ideal_values

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    crops = get_crop_list()
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
            crop_ideal_values = get_ideal_values(crop, growth_stage)
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
@app.route('/add_crop', methods=['GET', 'POST'])
def add_crop():
    if request.method == 'POST':
        try:
            # Extract form data
            crop_name = request.form['crop_name']
            
            # Prepare pre-fruit values
            pre_fruit = {}
            post_fruit = {}
            
            for param in ['N', 'P', 'K', 'temperature', 'humidity', 'pH', 'rainfall']:
                pre_fruit[param] = [
                    float(request.form[f'pre_{param}_min']),
                    float(request.form[f'pre_{param}_max'])
                ]
                post_fruit[param] = [
                    float(request.form[f'post_{param}_min']),
                    float(request.form[f'post_{param}_max'])
                ]
            
            # Add the new crop
            add_new_crop(crop_name, pre_fruit, post_fruit)
            flash(f'Crop "{crop_name}" added successfully!', 'success')
            return redirect(url_for('index'))
            
        except ValueError as e:
            flash(str(e), 'danger')
        except Exception as e:
            flash(f'Error adding crop: {str(e)}', 'danger')
    
    return render_template('add_crop.html')

@app.route('/manage_crops')
def manage_crops():
    return render_template('add_crop.html')

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