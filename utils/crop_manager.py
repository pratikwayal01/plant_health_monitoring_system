import json
import os
from pathlib import Path

# Path to the JSON file
JSON_FILE = Path(__file__).parent.parent / 'ideal_values.json'

def load_ideal_values():
    """Load ideal values from JSON file"""
    if not JSON_FILE.exists():
        # Create empty file if it doesn't exist
        JSON_FILE.write_text('{}')
        return {}
    
    with open(JSON_FILE, 'r') as f:
        return json.load(f)

def save_ideal_values(data):
    """Save ideal values to JSON file"""
    with open(JSON_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_new_crop(crop_name, pre_fruit_values, post_fruit_values):
    """Add a new crop with its ideal values"""
    data = load_ideal_values()
    
    # Validate the crop doesn't already exist
    if crop_name in data:
        raise ValueError(f"Crop '{crop_name}' already exists")
    
    # Validate the structure of the values
    required_params = ['N', 'P', 'K', 'temperature', 'humidity', 'pH', 'rainfall']
    for stage_values in [pre_fruit_values, post_fruit_values]:
        if not all(param in stage_values for param in required_params):
            raise ValueError(f"Missing required parameters. Needed: {required_params}")
        
        for param, values in stage_values.items():
            if not isinstance(values, list) or len(values) != 2:
                raise ValueError(f"Parameter {param} must be a list of two values [min, max]")
            if values[0] >= values[1]:
                raise ValueError(f"Parameter {param} must have min < max")
    
    # Add the new crop
    data[crop_name] = {
        "pre-fruit": pre_fruit_values,
        "post-fruit": post_fruit_values
    }
    
    save_ideal_values(data)
    return True

def get_crop_list():
    """Get list of available crops"""
    data = load_ideal_values()
    return list(data.keys())

def get_ideal_values(crop, growth_stage):
    """Get ideal values for specific crop and growth stage"""
    data = load_ideal_values()
    return data.get(crop, {}).get(growth_stage, None)