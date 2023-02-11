import requests

url = 'http://www.omdbapi.com/?i=tt5580390&apikey=2da3c928'

response = requests.get(url)

#print(response.json())



u = '45,333,888'

w = u.split(',')

v = ''

print(int(w[2])*10)


L = ['a', 'b', 1,2]

L[0] = 'C'

print(L)

if j == runtime_index:
    # data_values[j] = int(value.split(' ')[0])
    #print('It is working')
#elif j == award_winds_index:
    #data_values[j] = int(value.split(' ')[3])
    data_values.insert(j + 1, int(value.split(' ')[6]))
elif j == box_office_index:
    figure = value.split('$')[1]
    fig_parts = figure.split(',')
    data_values[j] = int(fig_parts[2]) + int(fig_parts[1]) * 1000 + int(fig_parts[0]) * 1000000
else:
    j += 1
    continue
print(data_values)





