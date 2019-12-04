from Markov import Markov
import numpy as np

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}
data = np.genfromtxt('weather.csv', delimiter = ',')
results = {}

for city, weather in city_weather.items():
    this_city = Markov(weather)
    this_city.load_data(data)
    this_city.day_zero_weather = weather
    results[city] = this_city.get_weather_for_day(7, 100)

for city, weather in results.items():
    print(city + ": " + str(weather))

for city, weather in results.items():
    res = max(weather, key = weather.get)
    print(city + ": " + res)
