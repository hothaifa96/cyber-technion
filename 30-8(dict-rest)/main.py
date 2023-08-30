d1 = {'rawad': 90, 'adi': 91, 'haitham': 100}
#
# print(d1)
# # {'rawad': 90, 'adi': 91, 'haitham': '100'}
# print(type(d1))
# # <class 'dict'>
# print(d1['rawad'])
# # 90
# print(d1['adi'])
# # 91
# d1['adi'] = 100
# print(d1['adi'])
# # 100

# print(d1.get('haitham'))  # try to receive the data else return none
# print(d1['haitham'])  # get the data if key exists or raise exception
# print(d1.get('razi'))  # None
# print(d1)
# # d1.pop('haitham') # delete by key
# # d1.clear() # delete all the dict
# x = d1.popitem()
# print(d1)
# print(x)

d1['talea'] = 94
d1['shiraz'] = 100
d1['shiraz '] = 10
d1['sharaf'] = 22
# print(d1)
# print(list(d1.keys()))
# print(list(d1.values()))
# print(list(d1.items()))

# if 'sharaf' in d1.keys():
#     print(d1['sharaf'])

# for k in d1.keys():
#     print(f'the new grade of {k},{d1[k]-10}')
#     d1[k] -= 10
#
# print(d1)


# for k in d1.keys():
#     print(k)
# for v in d1.values():
#     print(v)
#
# for k, v in d1.items():
#     print(f'{k} --> {v}')

# print the name of the gin in the class
# for -> str list set tuple range
print(d1.items())
max1 = ['', 0]

for name, grade in d1.items():
    if grade > max1[1]:
        max1[1] = grade
        max1[0] = name

print(max1[0])

# print(list(d1.keys())[list(d1.values()).index(max(list(d1.values())))])
