import requests

url = 'http://www.omdbapi.com/?i=tt5580390&apikey=2da3c928'

response = requests.get(url)

print(response.json())




