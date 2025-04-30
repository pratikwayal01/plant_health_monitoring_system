"""
Configuration settings for the Plant Health Monitoring System
"""

# OpenWeather API configuration
OPENWEATHER_API_KEY = "fa8001787aaaec74c21049d7261f0f57"  # Replace with your actual API key
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# General application settings
SECRET_KEY = "plant-health-monitoring-system-2025"  # For Flask sessions
DEBUG = True
TESTING = False

# File upload settings
ALLOWED_EXTENSIONS = {'csv'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# Weather alerts thresholds
TEMPERATURE_HIGH_THRESHOLD = 35  # °C
TEMPERATURE_LOW_THRESHOLD = 10   # °C
RAINFALL_HEAVY_THRESHOLD = 50    # mm
RAINFALL_DROUGHT_THRESHOLD = 5   # mm