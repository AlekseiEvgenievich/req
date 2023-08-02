import requests

names_cities = ("Лондон", "Шереметьево", "Череповец")

for city in names_cities:
    url_temp = "https://wttr.in/{}?nTqm&lang=ru"
    url = url_temp.format(city)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
