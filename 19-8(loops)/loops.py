# loops
# DRY - don't repeat yourself

# x = list(range(0, 16,3))
# print(x)

# print(list(range(2, 100, 2)))  # all the even numbers
# print(list(range(-100, 100, 10)))  # all the even numbers
# print(list(range(20, 0,-1)))  # all the even numbers
#
# # print all the divisions of 11 between 0 and 666
# print(list(range(0, 666, 11)))  #

# for
# lists tuples sets string range

# numbers = [19, 50, 'hodi', 'barak obama', 'sharam el shikh',True]
#
# for i in numbers:
#     print(i)


# for i in range(10):  # [0-9]
#     x = int(input('enter a number'))
#     print(x / 100)

# line1 = 'we WeRe oN a bReak !!'
#
# for lt in line1:
#     if lt.isupper():
#         print(line1.index(lt))

# write a python code to receive 5 number from the user
# print the sum of the numbers
# print the avg of the numbers
# print the max number

# sum = 0
# max = None
# counter = 0
# for i in range(5):
#     x = int(input('enter a number :'))
#     sum += x
#     counter += 1
#     if max is None or x > max:
#         max = x
#
# print(sum)
# print(sum / counter)
# print(max)

# inputs = []
#
# for i in range(5):
#     x = int(input('number : '))
#     inputs.append(x)
#
# print(inputs)
# print(sum(inputs))
# print(sum(inputs) / len(inputs))
# print(max(inputs))


# exercises
#  e1 - Write a Python program to find those numbers which are divisible by 7
#  and multiples of 5, between 1500 and 2700 (both included)
#
# for i in range(1500, 2701):
#     if not i % 7 and not i % 5:
#         print(i)

# e2 - Write a Python program that accepts a word from the user and reverses it.
# word = input('please enter a word to reverse')
# print(word[::-1])

# e3 -  Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5

# numbers = list(range(1, 10))
# odd_counter = 0
# even_counter = 0
#
# for number in numbers:
#     if number % 2 == 0:
#         even_counter += 1
#     else:
#         odd_counter += 1
#
# print(f'the number of the odd numbers is {odd_counter}', end=' ')
# print(f'the number of the even numbers is {even_counter}')


# e4 Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# for i in range(7):
#     if i not in [3, 6]:  # if i != 6 or i != 3
#         print(i)

# e5 Write a Python program to remove duplicates from a list.
#
# l1 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 22, 2, 4, 99, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 6, 6, 6, 66]
#
# s1 = set(l1)
# print(s1)


# for i in range(1,100):
#     if i % 10 == 0:
#         break
#     print(i)

#
# for i in range(60):
#     if i == 57:
#         break
#     print(i)
# else:
#     print('inside the else')fa