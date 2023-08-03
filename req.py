import requests

names_cities = ("Лондон", "Шереметьево", "Череповец")
payload = {"nTqm": "", "lang": "ru"}

for city in names_cities:
    url_temp = "https://wttr.in/{}"
    url = url_temp.format(city)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
