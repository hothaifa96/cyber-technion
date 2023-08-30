# 1 - Write a Python script to sort (ascending and descending)
# a dictionary by value.
import operator

q1 = {'a': 41, 'b': 55, 'c': 1, 'd': -92, 'e': 101, 'f': 68}
# {'d': -92,'c': 1,'a': 41,'b': 55,'f': 68,'e': 101}
list_q1_asc = sorted(q1.items(),key=operator.itemgetter(1))
print(dict(list_q1_asc))
list_q1_desc = sorted(q1.items(), key=operator.itemgetter(1)
                      ,reverse=True)
# list -> dict [] -> {}
print(dict(list_q1_desc))

# 2. Write a Python script to add a key to a dictionary.
#
# Sample Dictionary : {'0': 10, '1': 20}
# Expected Result : {'0': 10, '1': 20, '2': 30}

# 3. Write a Python script to concatenate the following
#   dictionaries to create a new one.
#
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# 4. Write a Python script to check whether a given
# key already exists in a dictionary.
