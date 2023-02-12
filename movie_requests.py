import requests, csv, pdb

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
    if response.status_code == 200:
        movie_data = response.json()
        return movie_data
    elif response.status_code == 404:
        print("The requested resource was not found on the server")
        return False
    elif response.status_code == 500:
        print("An error occurred on the server")
        return False
    else:
        print("Unexpected response:", response.status_code)
        return False


print(request('tt5580390'))


header = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations', 'Box Office']

with open('movies.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(header)



a = cleaner(data)


new_data = request(a['Parasite'])

#print(new_data)

def clean_movie(data):
    data_keys = []
    data_values = []
    for keys in data.keys():
        data_keys.append(keys)
    for values in data.values():
        data_values.append(values)
    for k in data_keys:
        if k == 'Title':
            data_keys[data_keys.index(k)] = 'Movie Title'
        elif k == 'Awards':
            data_keys[data_keys.index(k)] = 'Award Wins'
        elif k == 'BoxOffice':
            data_keys[data_keys.index(k)] = 'Box Office'
        else:
            continue
    i = data_keys.index('Poster')
    data_keys.insert(i,'Award Nominations')
    #Now I will create the data_values list
    runtime_index = data_keys.index('Runtime')
    award_winds_index = data_keys.index('Award Wins')
    award_nominations_index = award_winds_index + 1
    box_office_index = data_keys.index('Box Office')
    j = 0
    #pdb.set_trace()
    for value in data_values:
        if j == runtime_index:
            data_values[j] = int(value.split(' ')[0])
            j += 1
        elif j == award_winds_index:
            data_values[j] = int(value.split(' ')[3])
            data_values.insert(j + 1, int(value.split(' ')[6]))
            j += 1
        elif j == box_office_index:
            figure = value.split('$')[1]
            fig_parts = figure.split(',')
            data_values[j] = int(fig_parts[2]) + int(fig_parts[1]) * 1000 + int(fig_parts[0]) * 1000000
            j += 1
        else:
            j += 1
            continue
    # I am going to get only the basic data asked for the movies.csv file
    final_values = []
    k = 0

    for value in data_values:
        if k == data_keys.index('Movie Title'):
            final_values.append(value)
            k += 1
        elif k == runtime_index:
            final_values.append(value)
            k += 1
        elif k == data_keys.index('Genre'):
            final_values.append(value)
            k += 1
        elif k == award_winds_index:
            final_values.append(value)
            k += 1
        elif k == award_winds_index + 1:
            final_values.append(value)
            k += 1
        elif k == box_office_index:
            final_values.append(value)
            k += 1
        else:
            k += 1
            continue

    return final_values



def main():
    print('''MAIN MENU
    \r Select one of the options below: 
    a) Getting information from a movie
    b) Quit the App''')
    while ValueError:
        try:
            choice = input().lower()
            if choice != 'a' and choice !='b':
                raise ValueError('You must enter the letter associated with each option, such as "a"')
        except ValueError as err:
            print(f'{err}')
        else:
            movie_data = ''
            while movie_data == False or movie_data == '':
                id = input('Welcome, would you so kind to indicate me the ID of the movie you want to know about?')
                movie_data = request(id)
                break
                pass





# Ask for info
# Clean it
#Add it to the csv
# End of the point 6

#clean_movie(new_data)


if __name__ == "__main__":
    main()


        #Choose the id from the list
        #then clean the data
        #Add the data to the csv file
        #Create a menu (1. Select movie 2. Quit --> List of movies (IDs) 2. Quit









