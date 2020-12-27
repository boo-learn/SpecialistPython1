import json
import pprint
import urllib.request
app_id = '90dcc46f'
app_key = 'e16e576ca2c39bdbb28ccac2bdf6ce5a'


def get_data(url):
    json_data = urllib.request.urlopen(url).read()
    data = json.loads(json_data)
    return data


data = get_data("http://ip-api.com/json/")
lat = data['lat']
lon = data['lon']
weather_data = get_data(f"http://api.weatherunlocked.com/api/current/{lat},{lon}?app_id={app_id}&app_key={app_key}")
pprint.pprint(data)
pprint.pprint(weather_data)

city = data['city']
wx_desc = weather_data['wx_desc']
temp_c = weather_data['temp_c']
windspd_kts = weather_data['windspd_kts']
humid_pct = weather_data['humid_pct']
str = f"""
Погода сейчас в {city}
{wx_desc}
Температура: {temp_c} ℃
Ветер: {windspd_kts} км/ч
Влажность: {humid_pct} %
"""
print(str)
