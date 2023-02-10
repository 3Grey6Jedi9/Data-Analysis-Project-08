import requests, csv

from movieapi import api_key


with open('oscar_winners.csv', 'r') as file:
    data = file.read()



def cleaner(data):
    data_list = data.split('\n')
    data_list.pop(0)
    movie = {}
    for m in data_list:
        movie[m.split(',')[0]] = m.split(',')[1]
    return movie



def request(id):
    response = ''
    url = 'http://www.omdbapi.com/?' + 'i=' + id + '&apikey=' + api_key
    response = requests.get(url)
    movie_data = response.json()
    return movie_data


filename = 'movies.csv'

#with open(filename, 'a') as file:
    #writer


a = cleaner(data)


print(request(a['Parasite']))

def clean_movie(data):
    for k, v in data.items():
        if k == 'Runtime':
            data[k]=int(v.split(' ')[0])
        elif k == ''
        else:
            continue
            






