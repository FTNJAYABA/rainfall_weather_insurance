import requests
import datetime

API_KEY = 'your_openweathermap_api_key'

def get_rainfall(latitude, longitude, date):
    # Convert the date to a Unix timestamp
    timestamp = int(datetime.datetime.strptime(date, '%Y-%m-%d').timestamp())

    # OpenWeatherMap One Call API endpoint
    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine"

    # Parameters for the API request
    params = {
        'lat': latitude,
        'lon': longitude,
        'dt': timestamp,
        'appid': API_KEY
    }

    # Make the API request
    response = requests.get(url, params=params)
    data = response.json()

    # Extract rainfall data
    if 'current' in data and 'rain' in data['current']:
        rainfall = data['current']['rain'].get('1h', 0)
        print(f"Rainfall on {date} at ({latitude}, {longitude}): {rainfall} mm")
    else:
        print(f"No rainfall data available for {date} at ({latitude}, {longitude})")

if __name__ == "__main__":
    # Get user input for latitude, longitude, and date
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    date = input("Enter date (YYYY-MM-DD): ")

    # Fetch and display rainfall data
    get_rainfall(latitude, longitude, date)