import numpy as np

class Markov:
    def __init__(self, day_zero_weather = None):
        self.day_zero_weather = day_zero_weather
        self.types = ["sunny", "cloudy", "rainy", "snowy", "windy", "hailing"]
        self._current_day_weather = 0
        self._current_day = 0
        self.days = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_day > self.days:
            raise ValueError("The interation number exceeds the limit.")
        else:
            self._current_day_weather = np.random.choice(len(self.types), 1, p = self.data[self._current_day_weather])[0]
        self._current_day += 1
        return self.types[self._current_day_weather]

    def load_data(self, types):
        self.data = types

    def get_prob(self, current_day_weather, next_day_weather):
        if current_day_weather not in self.types:
            raise Exception("current_day_weather is not one of the 6 strings specified.")
        if next_day_weather not in self.types:
            raise Exception("next_day_weather is not one of the 6 strings specified.")
        row = self.types.index(current_day_weather)
        column = self.types.index(next_day_weather)
        return self.data[row, column]

    def _simulate_weather_for_day(self, day):
        self.days = day
        self._current_day = 0
        self._current_day_weather = self.types.index(self.day_zero_weather)
        for i in range(day):
            prediction = self.__next__()
        return prediction

    def get_weather_for_day(self, day, trials = 100):
        if (self.day_zero_weather == None):
            raise Exception("No day_zero_weather is given.")
        list_weather = {type: 0 for type in self.types}
        for i in range(trials):
            result_type = self._simulate_weather_for_day(day)
            list_weather[result_type] += 1
        return list_weather
