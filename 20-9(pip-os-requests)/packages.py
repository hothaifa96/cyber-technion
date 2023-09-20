# pip install <package name>
# pip uninstall <package name>
# pip list
# pip freeze

import requests

url = 'https://jsonplaceholder.typicode.com/users'

res = requests.get(url)

print(res.status_code)
if res.status_code == 200:
    print('the website is working')
    users = res.json()
    print(f'users the type is {type(users)}')
    for user in users:
        if user['name'][0].lower() == 'c':
            print(user)

else:
    print('Failed to retrieve data')

# # retrieve

#-------------- exercise ---------------
#write a python code to send get http request to https://jsonplaceholder.typicode.com/albums   and print all the albums title into the console

# res = requests.get('https://jsonplaceholder.typicode.com/albums')
#
# albums = res.json()
#
# for album in albums:
#     print(album['title'])
