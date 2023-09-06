# DRY - don't repeat yourself
import datetime
import os


# def <function name>():
#     function body

def greet():
    print('hello')


def greet_with_name(name):
    print(f'hello {name}')


def greet_name_age(name, age=18):
    print(f'hello {name} and you are {age} years old')


def my_sum(*args):
    s = 0
    for x in args:
        s += x
    print(s)


def greet_class(*args):
    print(args)
    for name in args:
        greet_with_name(name)


def foo(**kwargs):
    print(kwargs)
    print(type(kwargs))


#
#
# # greet()
# # n = input('enter your name')
# # greet_with_name(n)
# # greet_name_age(n, 11)
# # greet_name_age(n)
# # greet_name_age(age=19, name='yasta')
# my_sum(1, 2, 3, 4, 5, 7)
# greet_class('mahmod', 'shiraz', 'haitham', 'noor')
# foo(name='yahoo', age=11, webiste='linkedin.com/in/hothaifazoubi')


def calc_area(r):
    area = 3.14 * r ** 2
    return area


r1 = 5
r2 = 10
a1 = calc_area(r1)
a2 = calc_area(r2)

print(a1+a2)

print(datetime.datetime.now())