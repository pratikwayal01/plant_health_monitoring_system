"""
Weather API integration for the Plant Health Monitoring System
"""
import requests
from datetime import datetime
import sys
import os

# Add the project root to the path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OPENWEATHER_API_KEY, OPENWEATHER_BASE_URL
from config import TEMPERATURE_HIGH_THRESHOLD, TEMPERATURE_LOW_THRESHOLD
from config import RAINFALL_HEAVY_THRESHOLD, RAINFALL_DROUGHT_THRESHOLD


def get_weather_data(city):
    """
    Get current weather data for a given city using OpenWeather API
    
    Args:
        city (str): Name of the city
        
    Returns:
        dict: Weather data and alerts
    """
    # Handle empty city name
    if not city:
        return {
            'error': 'No city provided',
            'weather': None,
            'alerts': []
        }
    
    try:
        # Make API request
        params = {
            'q': city,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric'  # Use metric units (Celsius, mm, etc.)
        }
        
        # If using a test API key, return mock data
        if OPENWEATHER_API_KEY == "YOUR_API_KEY_HERE":
            return generate_mock_weather_data(city)
        
        response = requests.get(OPENWEATHER_BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses
        
        weather_data = response.json()
        
        # Extract relevant information
        processed_data = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
            'wind_speed': weather_data['wind']['speed'],
            'clouds': weather_data['clouds']['all'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Check for rain data (may not be present)
        if 'rain' in weather_data and '3h' in weather_data['rain']:
            processed_data['rainfall_3h'] = weather_data['rain']['3h']
        else:
            processed_data['rainfall_3h'] = 0
        
        # Generate weather alerts
        alerts = generate_weather_alerts(processed_data)
        
        return {
            'weather': processed_data,
            'alerts': alerts
        }
        
    except requests.exceptions.RequestException as e:
        return {
            'error': f"Weather API error: {str(e)}",
            'weather': None,
            'alerts': []
        }


def generate_weather_alerts(weather_data):
    """
    Generate farmer-friendly alerts based on weather conditions
    
    Args:
        weather_data (dict): Processed weather data
        
    Returns:
        list: Weather alerts
    """
    alerts = []
    
    # Temperature alerts
    temp = weather_data['temperature']
    if temp > TEMPERATURE_HIGH_THRESHOLD:
        alerts.append({
            'type': 'temperature',
            'severity': 'warning',
            'message': f"High temperature alert: {temp}°C may cause heat stress to plants",
            'recommendation': "Increase irrigation and consider adding shade"
        })
    elif temp < TEMPERATURE_LOW_THRESHOLD:
        alerts.append({
            'type': 'temperature',
            'severity': 'warning',
            'message': f"Low temperature alert: {temp}°C may slow down plant growth",
            'recommendation': "Consider protective coverings if frost is expected"
        })
    
    # Rain alerts (if available)
    if 'rainfall_3h' in weather_data:
        rainfall = weather_data['rainfall_3h']
        if rainfall > RAINFALL_HEAVY_THRESHOLD:
            alerts.append({
                'type': 'rainfall',
                'severity': 'warning',
                'message': f"Heavy rainfall alert: {rainfall}mm in the last 3 hours",
                'recommendation': "Check field drainage and watch for erosion"
            })
        elif rainfall < RAINFALL_DROUGHT_THRESHOLD and weather_data['humidity'] < 40:
            alerts.append({
                'type': 'rainfall',
                'severity': 'info',
                'message': "Low rainfall and humidity conditions detected",
                'recommendation': "Consider increasing irrigation frequency"
            })
    
    # Wind alerts
    if weather_data['wind_speed'] > 10:  # m/s
        alerts.append({
            'type': 'wind',
            'severity': 'info',
            'message': f"High wind speeds detected: {weather_data['wind_speed']} m/s",
            'recommendation': "Secure any loose structures and check for plant damage"
        })
    
    # Weather condition alerts
    description = weather_data['description'].lower()
    if 'thunderstorm' in description:
        alerts.append({
            'type': 'storm',
            'severity': 'warning',
            'message': "Thunderstorm conditions detected",
            'recommendation': "Watch for lightning strikes and potential flooding"
        })
    elif 'snow' in description:
        alerts.append({
            'type': 'snow',
            'severity': 'warning',
            'message': "Snowy conditions detected",
            'recommendation': "Protect sensitive crops from frost and snow weight"
        })
    
    return alerts


def generate_mock_weather_data(city):
    """
    Generate mock weather data for testing when API key is not available
    
    Args:
        city (str): Name of the city
        
    Returns:
        dict: Mock weather data
    """
    import random
    
    # Generate realistic but random weather data
    temp = round(random.uniform(15, 30), 1)
    humidity = random.randint(40, 90)
    
    # Weather descriptions
    descriptions = [
        "clear sky", "few clouds", "scattered clouds", 
        "broken clouds", "shower rain", "rain", 
        "thunderstorm", "mist", "light rain"
    ]
    
    # Icon codes
    icons = ["01d", "02d", "03d", "04d", "09d", "10d", "11d", "50d"]
    
    # Choose description and matching icon
    description = random.choice(descriptions)
    # In a real implementation, we would match the icon to the description
    icon = random.choice(icons)
    
    # Create mock weather data
    processed_data = {
        'city': city,
        'temperature': temp,
        'humidity': humidity,
        'description': description,
        'icon': icon,
        'wind_speed': round(random.uniform(0, 10), 1),
        'clouds': random.randint(0, 100),
        'rainfall_3h': round(random.uniform(0, 10), 1) if random.random() > 0.7 else 0,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Generate alerts
    alerts = generate_weather_alerts(processed_data)
    
    return {
        'weather': processed_data,
        'alerts': alerts,
        'note': 'This is mock weather data for testing. Replace OPENWEATHER_API_KEY in config.py with your actual API key.'
    }