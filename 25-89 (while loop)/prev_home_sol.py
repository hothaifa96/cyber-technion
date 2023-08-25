# Task 1:
# Write a program to print the numbers from 1 to 10 using a for loop.
import math

# for i in range(1, 11):
#     print(i, end=' ')

# Task 2:
# Print the even numbers between 1 and 20 using a for loop.
# sol 1
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, end=' ')
#
# sol2
# for i in range(2, 21, 2):
#     print(i, end=' ')

# Task 3:
# Print the squares of numbers from 1 to 10 using a for loop.

# for i in range(1, 11):
#     print(i ** 2, end=' ')

# Task 4:
# Write a program to calculate the sum of all numbers from 1 to 50 using a for loop.

# sum = 0
# for i in range(1, 51):
#     sum += i
#
# print(f'the sum of all the numbers is {sum}')

# Task 5:
# Print the Fibonacci sequence (first 10 numbers) using a for loop.
x = 0
# y = 1
#
# for i in range(10):
#     print(x, end=' ')
#     tmp = x
#     x = y
#     y = tmp + y


# Task 6:
# Create a program that checks if a given number is prime or not.

# number = int(input('please enter a number : '))
# is_prime = True
# for i in range(2, 11):
#     if number % i == 0:
#         is_prime = False
#
# print(is_prime)

#
# for i in range(2, 11):
#     if number % i == 0:
#         break
# else:
#     print('prime')

# Task 7:
# Print the factorial of a given number using a for loop

# # multi = 1
# number = int(input('please enter a number '))
# # for i in range(1,number+1):
# #     multi *=i
# #
# # print(f'the factorial is : {multi}')
#
# print(f'the factorial is : {math.factorial(number)}')
#


# Task 8:
# Generate a multiplication table for a given number using a for loop.

# n = int(input('enter a number :'))
#
# for i in range(1, 11):
#     print(f'{n} * {i} = {n * i}')

# Task 9:
# Write a program to print the following pattern using a nested for loop:
# *
# **
# ***
# ****

# for i in range(1,5):
#     for j in range(i):
#         print('*',end=' ')
# #     print()
# for i in range(100):
#     print('* '*i)


# Task 10:
# Print a right-angled triangle pattern using a nested for loop:
#    *
#   * *
#  * * *
# * * * *

# stars = int(input('please enter the number of the starts'))
# for i in range(1,stars):
#     print(' '*(stars-i),'* '*i)
# for i in range(2, stars):
#     print(' '*i,'* '*(stars-i))


# Task 11:
# Write a program that finds the maximum element in a list using a for loop.
# numbers = [22, 44, 15, 612, 77, 61, 61, 1, 1, 22222, 5, 6, 6, 6]
# # print(numbers)
# # my_max = numbers[0]
# # for number in numbers:
# #     if number > my_max:
# #         my_max = number
# # print(f'the max number is {my_max}')
# # print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# numbers.sort()


# Task 12:
# Calculate the average of numbers in a list using a for loop.
# numbers = []
# for i in range(5):
#     numbers.append(int(input('enter number')))
# print(numbers)
# avg = sum(numbers) // len(numbers)
# print(avg)
# Task 13:
# Write a program to find and print all the even numbers between two given numbers.

# Task 14:
# Create a program that simulates a basic calculator. It should take two numbers and an
# operator (+, -, *, /) as input and perform the corresponding operation.
# a = float(input('enter a number '))
# b = float(input('enter a number '))
# op = input('enter operator (+,-,/,*) :')
# if op == '+':
#     print(a + b)
# elif op == '/':
#     print(a / b if b > 0 else 'cannot divide by zero')
# elif op == '-':
#     print(a - b)
# elif op == '*':
#     print(a * b)

# Task 15:
# Write a program that generates a list of random numbers and then prints all the prime
# numbers from that list.

# import random
#
# # generate the list
# randoms = []
# for i in range(20):
#     randoms.append(random.randint(1, 100))
# print(randoms)
# # to print the prime numbers
# for number in randoms:
#     is_prime = True
#     for i in range(2, 11):
#         if number % i == 0 and number != i:
#             is_prime = False
#     if is_prime:
#         print(number)

# Task 16:
# Write a program that takes a sentence as input and counts the number of vowels and
# consonants.
# sen = input('enter a text ')
# vowels = 'aeoiu'
# vowels_count = 0
# consonants_count = 0
#
# for lt in sen:
#     if lt in vowels:
#         vowels_count +=1
#     else:
#         consonants_count+=1
# print(f'the vowels counter is :{vowels_count}')

# Task 17:
# Create a program that generates a list of integers and then finds the second-largest
# element in the list.
# Task 18:
# Write a program to check if a given string is a palindrome or not.
# name = 'radar'
# if name == name[::-1]:
#     print('palindrome')
# Task 19:
# Generate a list of numbers and then print only the numbers that are divisible by both 3
# and 5.
# Task 20:
# Write a program that simulates a simple quiz game. Create a list of questions along with
# their correct answers. Ask the user these questions one by one and keep track of their
# score.
q = ['what is the name of turing?',
     'what is dns?',
     'what is the subnet mask of this ip 188.15.78.9/16 as ip ?',
     'wht is the fastest protocol http tcp udp or ftp ?',
     'what is the name of the workers between thr RAM and the CPU ?']
ans = ['alan', 'domain name system', '255.255.0.0', 'udp', 'register']

score = 0

for i in range(len(q)):
    print(q[i])
    if ans[i] == input('enter your answer :'):
        score += 20

print(score)
