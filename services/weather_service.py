import requests
import matplotlib.pyplot as plt
import io

def fetch_weather_data(lat, lon):
    headers = {'User-Agent': 'MyWeatherApp'}
    url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        point_data = response.json()
        forecast_url = point_data['properties']['forecast']
        forecast_response = requests.get(forecast_url, headers=headers)

        if forecast_response.status_code == 200:
          return forecast_response.json()
        else: return 'Forecast response failed'
    
    return None

def generate_temperature_plot(weather_data):
    time_periods = [period['name'] for period in weather_data['properties']['periods']]
    temperatures = [period['temperature'] for period in weather_data['properties']['periods']]

    plt.figure(figsize=(15, 10))

    plt.plot(time_periods, temperatures, marker='o')
    plt.xlabel('Period')
    plt.ylabel('Temperature (F)')
    plt.title('Temperature in Seattle')
    plt.xticks(rotation=45)

    file_path = "static/temperature_plot.png"
    plt.savefig(file_path)
    plt.close
    
    return file_path
