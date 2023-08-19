#
# if condition1:
#     # condition 1 True block
# elif condotion2:
#     # condition 1 false block and condition 2 true
# else:
#     #false block
#


# >
# <
# >=
# <=
# ==
# !=
# not
# and
# or
# 'hod'.is

# x = int(input('please enter number : '))
#
# if x % 7 == 0:
#     print('got it')
#
# print('got it' if x % 7 == 0 else 'try another number')

# Write a Python program to get a number from the user
# For multiples of three
# print "Fizz" instead of the number and
# for multiples of five print "Buzz".
# For numbers that are multiples of three and five,
# print "FizzBuzz". Hint %

# 3 -> Fizz
# 10 -> Buzz
# 30 -> FizzBuzz

# number = int(input('enter a number : '))
# # if number % 5 == 0 and number % 3 == 0:
# #     print('FizzBuzz')
# # elif number % 5 == 0:
# #     print('Buzz')
# # elif number % 3 == 0:
# #     print('Fizz')
# ans = ''
# if number % 3 == 0:
#     ans += 'Fizz'
# if number % 5 == 0:
#     ans += 'Buzz'
#
# print(ans)
#
# print(
#     'FizzBuzz' if not number % 3 and not number % 5
#     else 'Fizz' if not number % 3
#     else 'Buzz' if not number % 5
#     else '')
