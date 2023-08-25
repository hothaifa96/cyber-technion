# loop

# DRY - dont repeat yourself

# for -> n iterations

# write a code to ask the user for a password
# the currect password is 'shawarma'
# write a code thats keeps taking password until the user
# enter shawarma

# while -> loop thats iterate per condition

# sum = 0
# while sum < 100:
#     sum+=int(input('enter a number'))
#
# print(sum)

# x = 5
# while x != 8:
#     x = int(input('guess the number'))
#     if x<0 :
#         break
#     print(x)

# do-while


# while True:
#     password = input('please enter your password')
#     if password == 'shawarma':
#         break
#     print('eeeeeeh this is a wrong password')
#
# print('welcome to your application ')

# factorial
# 5! = 1 * 2 * 3 * 4 * 5

# n=5
# factorial = 1
#
# for i in range(1,n+1):
#     factorial *=i
# print(factorial)

# n = int(input('enter a number'))
#
# factorial = 1
# while n > 0:
#     factorial *= n
#     n -= 1
# print(factorial)
# 5! = 1*2*3*4*5
# 5! = 5*4*3*2*1

# import math
#
# print(math.factorial(6))

# word = 'bmw z4'
# lives = 6
# guesses=[]
# while len(word) != 0:
#     print(guesses)
#     char = input('enter a char ')
#     guesses.append(char)
#     if char in word:
#         print('bingo ')
#         word = word.replace(char, '', 1)
#     else:
#         lives -= 1
#         print(f'you have {lives} left')
#     if lives == 0:
#         print('game over ')
#         break



