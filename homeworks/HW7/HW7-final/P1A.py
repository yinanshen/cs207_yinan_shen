from Markov import Markov
import numpy as np

weather = np.genfromtxt('weather.csv', delimiter = ',')
weather_today = Markov()
weather_today.load_data(weather)
print(weather_today.get_prob('cloudy', 'windy'))
