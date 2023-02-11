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

#Separete the dictionary into two different lists then clean the data and put the data into a CSV file

#def clean_movie(data):
    #for k, v in data.items():
        #if k == 'Runtime':
            #data[k]=int(v.split(' ')[0])
        #elif k == 'Awards':
            #data[k] = int(v.split(' ')[3])
            #k = 'Award Wins'
            #data['Award Nominations'] = int(v.split(' ')[6])
        #elif k == 'BoxOffice':
            #a = v.split('$')[1]
            #b = a.split(',')
            #data[k] = int(b[2]) + int(b[1])*1000 + int(b[0])*1000000
            #k = 'Box Office'
        #else:
            #continue
    #return data

#print(clean_movie(request(a['Parasite'])))

# Do it using a list





