import requests

# {GET POST PUT DELETE - API}
#
# url = 'https://www.boredapi.com/api/activity'
# res = requests.get(url)
#
# if res.status_code == 200 :
#     print('success')
# else:
#     print('its been a long day ...... ')


# 2
#
# url = 'https://www.boredapi.com/api/activity'
#
# for i in range(5):
#     res = requests.get(url)
#     data = res.json()
#     print(data['activity'],' -> ',data['participants'])

#
# url = 'http://www.boredapi.com/api/activity?participants=2'
#
# for i in range(5):
#     res = requests.get(url)
#     data = res.json()
#     print(data['activity'],' -> ',data['participants'])

url = 'http://www.boredapi.com/api/activity?maxprice=1&type=social&participants=2'

for i in range(5):
    res = requests.get(url)
    data = res.json()
    print(data['key'])
