# pip install <package name>
# pip uninstall <package name>
# pip list
# pip freeze

import requests

#
# url = 'https://jsonplaceholder.typicode.com/users'
#
# res = requests.get(url)
#
# print(res.status_code)
# if res.status_code == 200:
#     print('the website is working')
#     users = res.json()
#     print(f'users the type is {type(users)}')
#     for user in users:
#         if user['name'][0].lower() == 'c':
#             print(user)
#
# else:
#     print('Failed to retrieve data')

# # retrieve

# -------------- exercise ---------------
# write a python code to send get http request to https://jsonplaceholder.typicode.com/albums   and print all the albums title into the console

# res = requests.get('https://jsonplaceholder.typicode.com/albums')
#
# albums = res.json()
#
# for album in albums:
#     print(album['title'])

# ------------------- exercise 2 -------------------------

# Write a Python script that performs the following tasks using the requests library:
#
# a. Send an HTTP GET request to the JSONPlaceholder API's /users endpoint to retrieve a list of users.

res = requests.get('https://jsonplaceholder.typicode.com/users')

# b. Check if the request was successful by examining the response's status code.

if res.status_code == 200:
    print('success')
    # c. If the request was successful (status code 200), parse the JSON data in the response.
    data = res.json()

    # d. Display the following information for each user:
    # User ID
    # Name
    # Email
    # Phone
    for user in data:
        print(f'user id -> {user["id"]}  ', end='')
        print(f'name -> {user["name"]}  ', end='')
        print(f'email -> {user["email"]}  ', end='')
        print(f'phone -> {user["phone"]}  ')

    # e. Filter and display only the users  with lat between 25.0 35.0
    my_users = [user for user in data if 0.0 < float(user['address']['geo']['lat']) < 35.0]
    # for user in data:
    #     if 0.0 < float(user['address']['geo']['lat']) < 35.0:
    #         my_users.append(user)
    print(my_users)
    # f. Calculate and display the total number of users retrieved from the the previous task
    print(len(my_users))
