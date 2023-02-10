import requests, csv

from movieapi import api_key


with open('oscar_winners.csv', 'r') as file:
    data = file.read()



def cleaner(data):
    data_list = data.split('\n')
    data_list.pop(0)
    movies = {}
    for movie in data_list:
        movies[movie.split(',')[0]] = movie.split(',')[1]
    return movies



def request(id):
    response = ''
    url = 'http://www.omdbapi.com/?' + 'i=' + id + '&apikey=' + api_key
    response = requests.get(url)
    print(response.json())


#a = cleaner(data)


#request(a['Parasite'])



