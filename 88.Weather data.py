#Weather data

import requests
try:
    api_address ="https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    city = input("City name")
    url = api_address + city
    json_data = requests.get(url).json()
    formatted_data = json_data['base']
    print(formatted_data)

except:
    print("The city given is wrong!")