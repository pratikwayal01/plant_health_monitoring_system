# Plant Health Monitoring System

A Flask-based web application for monitoring plant health using IoT sensor data and weather information.

## Features

- Upload CSV data with plant sensor readings
- Analyze soil nutrients (N-P-K), temperature, humidity, pH, and rainfall
- Compare readings with ideal values for specific crops and growth stages
- Generate health status reports and recommendations
- Visualize sensor data trends with Chart.js
- Integrate with OpenWeather API for weather alerts

## Requirements

- Python 3.8+
- Flask
- Pandas
- Requests
- Chart.js (included via CDN)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/plant-health-monitoring-system.git
cd plant-health-monitoring-system
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure OpenWeather API:
   - Sign up at [OpenWeather](https://openweathermap.org/api) to get an API key
   - Update `config.py` with your API key

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

## Usage

1. Select a crop (e.g., Tomato, Wheat, Rice)
2. Choose a growth stage (pre-fruit or post-fruit)
3. Enter your location (city name)
4. Upload a CSV file with sensor data
5. View the generated report with health analysis, charts, and recommendations

## CSV Data Format

Your CSV file should include the following columns:
- `N` - Nitrogen ratio
- `P` - Phosphorus ratio
- `K` - Potassium ratio
- `temperature` - Temperature in °C
- `humidity` - Humidity in %
- `pH` - Soil pH level
- `rainfall` - Rainfall in mm
- `timestamp` - Date in YYYY-MM-DD format

## Sample CSV Data

A sample CSV file is included in the `data/` directory for testing.

## Project Structure

```
plant_health_monitoring_system/
├── app.py                  # Main Flask application
├── config.py               # Configuration (API keys, etc.)
├── static/
│   ├── css/
│   │   └── styles.css      # Custom styles
│   └── js/
│       └── charts.js       # Chart.js implementation
├── templates/
│   ├── index.html          # Main page with form
│   └── report.html         # Report page with charts and alerts
├── utils/
│   ├── __init__.py
│   ├── data_processor.py   # CSV processing
│   ├── health_analyzer.py  # Rule-based analysis
│   └── weather_api.py      # OpenWeather API integration
├── data/
│   └── sample.csv          # Sample data for testing
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

## License

MIT License# Rule-based-crop-monitoring
