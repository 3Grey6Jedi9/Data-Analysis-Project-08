import requests, csv

from movieapi import api_key


with open('oscar_winners.csv', 'r') as file:
    data = file.read()

#print(data.split('\n')[1].split(',')[1])

print(data.split('\n'))

data_list = data.split('\n')
data_list.pop(0)


movies = {}

for movie in data_list:
    movies[movie.split(',')[0]]=movie.split(',')[1]

print(movies)








def request(parameter):
    response = ''
    url = 'http://www.omdbapi.com/?' + parameter + '&apikey=' + api_key
    response = requests.get(url)
    print(response.json())




