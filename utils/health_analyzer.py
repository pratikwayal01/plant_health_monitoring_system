"""
Health analysis module for the Plant Health Monitoring System
"""

def analyze_health(processed_data, ideal_values):
    """
    Analyze plant health based on sensor data and ideal values
    
    Args:
        processed_data (dict): Processed sensor data
        ideal_values (dict): Ideal value ranges for each parameter
        
    Returns:
        dict: Health analysis results
    """
    if not ideal_values:
        return {
            'error': 'No ideal values found for this crop and growth stage'
        }
    
    latest_values = processed_data['latest_values']
    analysis = {
        'parameters': {},
        'overall_health': 'good',
        'alerts': []
    }
    
    # Define severity levels
    severity_levels = {
        'critical': 0,
        'warning': 0,
        'good': 0
    }
    
    # Analyze each parameter
    for param, value in latest_values.items():
        if param in ideal_values:
            min_val, max_val = ideal_values[param]
            
            # Check if value is within ideal range
            if min_val <= value <= max_val:
                status = 'good'
                message = f"{param} is within ideal range"
            elif value < min_val:
                # Calculate how far below minimum (as percentage)
                deviation = (min_val - value) / min_val * 100
                if deviation > 20:
                    status = 'critical'
                    message = f"{param} is critically low"
                else:
                    status = 'warning'
                    message = f"{param} is below ideal range"
            else:  # value > max_val
                # Calculate how far above maximum (as percentage)
                deviation = (value - max_val) / max_val * 100
                if deviation > 20:
                    status = 'critical'
                    message = f"{param} is critically high"
                else:
                    status = 'warning'
                    message = f"{param} is above ideal range"
            
            # Specific recommendations based on parameter
            recommendation = generate_recommendation(param, status, value, min_val, max_val)
            
            # Update severity counts
            severity_levels[status] += 1
            
            # Store parameter analysis
            analysis['parameters'][param] = {
                'value': value,
                'ideal_range': [min_val, max_val],
                'status': status,
                'message': message,
                'recommendation': recommendation
            }
            
            # Add to alerts if not good
            if status != 'good':
                analysis['alerts'].append({
                    'parameter': param,
                    'message': message,
                    'recommendation': recommendation,
                    'severity': status
                })
        
    # Determine overall health
    if severity_levels['critical'] > 0:
        analysis['overall_health'] = 'critical'
    elif severity_levels['warning'] > 0:
        analysis['overall_health'] = 'warning'
    # else remains 'good'
    
    # Sort alerts by severity (critical first, then warning)
    analysis['alerts'] = sorted(
        analysis['alerts'], 
        key=lambda x: 0 if x['severity'] == 'critical' else 1
    )
    
    return analysis


def generate_recommendation(param, status, value, min_val, max_val):
    """
    Generate parameter-specific recommendations
    
    Args:
        param (str): Parameter name
        status (str): Status (good, warning, critical)
        value (float): Current value
        min_val (float): Minimum ideal value
        max_val (float): Maximum ideal value
        
    Returns:
        str: Recommendation text
    """
    if status == 'good':
        return f"Continue maintaining current {param} levels"
    
    # Parameter-specific recommendations
    if param == 'N':
        if value < min_val:
            return "Apply nitrogen-rich fertilizer like urea or ammonium nitrate"
        else:
            return "Reduce nitrogen application and consider adding more carbon material"
    
    elif param == 'P':
        if value < min_val:
            return "Apply phosphorus-rich fertilizer like bone meal or rock phosphate"
        else:
            return "Reduce phosphorus application and consider testing soil pH"
    
    elif param == 'K':
        if value < min_val:
            return "Apply potassium-rich fertilizer like potassium chloride or wood ash"
        else:
            return "Reduce potassium application and monitor soil drainage"
    
    elif param == 'temperature':
        if value < min_val:
            return "Consider using row covers or greenhouse techniques to increase temperature"
        else:
            return "Provide shade or increase irrigation to reduce heat stress"
    
    elif param == 'humidity':
        if value < min_val:
            return "Increase irrigation or use mulch to retain moisture"
        else:
            return "Improve air circulation and reduce overhead watering"
    
    elif param == 'pH':
        if value < min_val:
            return "Apply agricultural lime to increase soil pH"
        else:
            return "Apply sulfur or acidifying fertilizers to reduce soil pH"
    
    elif param == 'rainfall':
        if value < min_val:
            return "Increase irrigation frequency"
        else:
            return "Improve drainage and reduce irrigation"
    
    # Default recommendation
    return "Monitor and adjust based on plant appearance and growth"