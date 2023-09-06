from flask import Flask, render_template, send_file, url_for
from services import weather_service

MyApp = Flask(__name__)

@MyApp.route("/")
def index():
	return render_template('index.html')

@MyApp.route("/seattle_weather")
def seattle_weather():
	lat, lon = 47.6062, -122.3321
	weather_data = weather_service.fetch_weather_data(lat, lon)

	if weather_data:
		img_path = weather_service.generate_temperature_plot(weather_data)
		return render_template('seattle_weather.html', img_url=img_path)
	else:
		return 'Failed to get weather data', 400

if __name__ == "__main__":
	MyApp.run()