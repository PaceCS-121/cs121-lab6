import json
import requests
import pandas as pd


def main():
    # load Pace's weather data
    weather_json = json.loads(requests.get('https://colabprod01.pace.edu/api/influx/sensordata/Odin/delta?days=1').text)
    weather = pd.json_normalize(weather_json)
    print(weather.head())

    # write your code here

    
    return

if __name__ == '__main__':
    main()