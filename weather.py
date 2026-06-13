import requests
url="https://api.openweathermap.org/data/2.5/weather?q=ahmedabad&appid=d7549fa26fcb7426e6cd9d0d48cc4370"
response=requests.get(url)
data=response.json()
print(data)