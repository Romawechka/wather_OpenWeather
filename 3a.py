"""
Author: https://github.com/Romawechka
Python version 3.8.5
"""

import requests
import json

API_KEY = 'API'

def weather():
    sity = input("Your sity\n")
    prefix = 'q'
    try:
        sity = int(sity)
        prefix = 'id'
    except ValueError:
        try:
            lat = float(sity.split()[0])
            sity = float(sity.split()[1])
            prefix = f'lat={lat}&lon'
        except ValueError:
            pass

    req = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?{prefix}={sity}&'
                       f'appid={API_KEY}&units=metric')

    my_json = req.content.decode('utf8')
    data = json.loads(my_json)

    if data["cod"] == '200':
        list_temp = []
        list_tempmax = []
        dt_txt = ''
        for el in data['list']:
            if el['dt_txt'].split()[0] != dt_txt and el['dt_txt'].split()[1] == '09:00:00':
                dt_txt = el['dt_txt'].split()[0]
                list_temp.append(float(el['main']['temp']))
                list_tempmax.append(float(el['main']['temp_max']))

        average = sum(list_temp) / len(list_temp)

        if not isinstance(sity, str):
            sity = data['city']['name']
        print(f'In your sity - {sity} for 5 days the morning temperature will be average: {round(average, 2)} °С'
              f' max: {round(max(list_tempmax), 2)} °С')

    else:
        print(data['message'])


if __name__ == "__main__":
    while True:
        weather()
        choice = input('\nIf you want to see the weather again, enter any message.'
                       ' If you want to exit enter "exit" or just close the application.\n')
        if choice == 'exit':
            exit()

# 59.8944 30.2642
# 498817
# Saint Petersburg
