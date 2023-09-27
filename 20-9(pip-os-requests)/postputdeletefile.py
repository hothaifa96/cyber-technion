import requests

# ------------ GET -------------

# get_url = 'https://httpbin.org/get'
#
# res = requests.get(get_url)
#
# print(res.status_code)
# print(res.text)

# ------------ POST -------------
# data = {'name': 'mazda', 'id': 144}
# post_url = 'https://httpbin.org/post'
# res = requests.post(post_url, data=data)
#
# print(res.status_code)
# print(res.text)

# ------------ put -------------
# data = {'name': 'tototo', 'id': 144}
# put_url = 'https://httpbin.org/put'
# res = requests.put(put_url, data=data)
#
# print(res.status_code)
# print(res.text)

#----------- DELETE ---------
res = requests.delete('https://httpbin.org/delete')

print(res.status_code)