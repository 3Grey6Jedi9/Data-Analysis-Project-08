import requests, csv, pdb, sys, os

from movieapi import api_key


#GETTING THE MOVIE'S INFO

with open('oscar_winners.csv', 'r') as file:
    data = file.read()


#CLEANING MOVIE'S INFO

def cleaner(data):
    '''It cleans the data provide from the movies so I can get the ID'''
    data_list = data.split('\n')
    data_list.pop(0)
    movie = {}
    for m in data_list:
        movie[m.split(',')[0]] = m.split(',')[1]
    return movie


#REQUESTING INFO TO THE API

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





header = ['Movie Title', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Award Wins', 'Award Nominations', 'Box Office']



#CLEANING THE MOVIE DATA RECIEVED BY THE API

# I need to get 3 more columns
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
            award_list = value.split(' ')
            data_values[j] = award_list[award_list.index('wins')-1]
            data_values.insert(j + 1, award_list[award_list.index('nominations')-1])
            j += 1
        elif j == box_office_index:
            if data_values[j] != 'N/A':
                figure = value.split('$')[1]
                fig_parts = figure.split(',')
                data_values[j] = int(fig_parts[2]) + int(fig_parts[1]) * 1000 + int(fig_parts[0]) * 1000000
                j += 1
            elif data_values[j] == 'N/A':
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
        elif k == data_keys.index('Rated'):
            final_values.append(value)
            k += 1
        elif k == data_keys.index('Released'):
            final_values.append(value)
            k += 1
        elif k == runtime_index:
            final_values.append(value)
            k += 1
        elif k == data_keys.index('Genre'):
            final_values.append(value)
            k += 1
        elif k == data_keys.index('Director'):
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



# A MENU FUNCTION JUST TO MAKE THINGS NEATER

def menu():
    print('''\n***   MAIN MENU   ***
        \r Select one of the options below: 
        a) Getting information from a movie
        b) Quit the App''')



# THE MAIN FUNCTION THAT RUNS THE APP



def main():
    app = True
    while app:
        menu()
        while ValueError:
            try:
                choice = input().lower()
                if choice != 'a' and choice !='b':
                    raise ValueError('You must enter the letter associated with each option, such as "a"')
                elif choice == 'b':
                    sys.exit()
            except ValueError as err:
                print(f'{err}')
            else:
                movie_data = ''
                while movie_data == False or movie_data == '':
                    i = 1
                    for key, value in cleaner(data).items():
                        print(f'{i}) {key}: {value}')
                        i += 1
                    nid = int(input('\nWould you so kind to indicate the ID of the movie you want to know about (enter the number associated)?\t'))
                    if nid in range(1,len(cleaner(data))+1):
                        j = 1
                        for value in cleaner(data).values():
                            if nid == j:
                                id = value
                                break
                            else:
                                j += 1
                                continue
                        movie_data = request(id)
                        data_row = clean_movie(movie_data)
                        print(data_row)
                        with open('movies.csv', 'a') as file:
                            writer = csv.writer(file)
                            if os.path.getsize("movies.csv") == 0:
                                writer.writerow(header)
                            writer.writerow(data_row)
                    else:
                        print('\nYou must enter a valid number please, try again\n')
                        movie_data = False
                    break
            break





if __name__ == "__main__":
    main()











