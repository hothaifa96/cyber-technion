# 1
# text = input('enter str')
# print(text,len(text))

# 2
# url = input('enter url')
#
# url = url.lower()
#
# print(f'a appeared {url.count("a")} times')
# print(f'b appeared {url.count("b")} times')
# print(f'c appeared {url.count("c")} times')
# 3
# text = input('enter str')
# print(text.upper())
#
# t = input('enter a long text')
#
# ans = t[0:3] + t[-3:]  # concat
# print(ans)

# 5
# q5 = input('enter a text')
# print(q5.isdigit())

# 6
#
# sen = input('please enter sen')
# word_to_replace = input('please enter old word ')
# new_word = input('please enter new word')
# print(sen)
# print(sen.replace(word_to_replace, new_word))

# 7
# word = input('enter somthing')
# print(word)
# print(word[::-1])

# 8
# word = input('enter somthing')
#
# print(f'is the word all upper {word.isupper()} or all lower {word.islower()}')

# 9

# name = input('enter your name : ')
# c = input('enter your c : ')
# age = input('enter your age : ')

# print(f'my name is {name} and im {age} years old  im from {c}')

# 10

text = 'hello world'
print(text)
text = text[:5] + 'f' + text[5:]
text = text[:4] + ' ' + text[4:]
text = text[-5:] + text[4:-5] + text[:4]
print(text)
