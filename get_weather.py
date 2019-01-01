#!/usr/local/bin/python3


from weather import Weather, Unit
from sys import argv


def get_weather(city):
    weather = Weather(unit = Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    condition = location.condition
    print(condition.text)
    print(condition.temp + '° C')


if len(argv) > 2:
    print('Please specify only one city')
elif len(argv) == 1:
    print('Please specify a city')
else:
    get_weather(argv[1])
