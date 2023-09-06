# 1 write a python function to print the area of triangle
# the function get b and h and returns the area
# b *h /2

# def calc_area(b, h):
#     return b * h / 2
#
#
# a1 = calc_area(6, 3)
# print(a1)

# 2 Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

# def multiply(numbers):
#     multi = 1
#     for number in numbers:
#         multi *= number
#     return multi
#
#
# list1 = [8, 2, 3, -1, 7]
# list2 = []
# for i in range(10):
#     list2.append(int(input('enter a number :')))
# m = multiply(list1)
# print(f'the multiply is :{m}')

# 3 Write a Python function that accepts a string
# and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count_letters(sentence):
    lower_c = 0
    upper_c = 0
    for lt in sentence:
        if lt.isupper():
            upper_c += 1
        elif lt.islower():
            lower_c += 1
    return upper_c, lower_c


upper, lower = count_letters('Live What You    Love .....')
print(f'the number of upper case characters : {upper}')
print(f'the number of lower case characters : {lower}')
