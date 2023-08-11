# write a python code  to receive an email from the user
# - print the length of the email (hint len())
# - print the domain of the email (gmail.com)
# - print each odd letter in the email using [start:end:step]
# - **challenge print the email 3 times in the same line
#
# email = input('please enter your mail : ')
# # length of the mail
# print(len(email))
# # print the domain
# print(email[email.find('@'):])
# # print odd letters
# print(email[1::2])
# print(email * 9)

# string exercises :

name = 'cristiano ronaldo'

# print(name[-5:])  # last 5 chars

# print(name[:len(name) // 3 + 1]) # prints the first third

# print(name.count('a'))  # number of 'a's in the name

# print('b' in name) # print whether the name contains the letter b

line= 'Hello World!'
print(line.find('o'))
print(line.rfind('o'))
print(line[:line.find('o')+1])
print(line[line.rfind('o'):])
print(line.replace('o',''))

