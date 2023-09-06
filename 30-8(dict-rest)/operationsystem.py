import os

# current working dir
# current_dir = os.getcwd()
# print(f'this dir is {current_dir}')

# content of dir
# path = '/Users/hothaifa/Desktop/pre/demo1'
# content = os.listdir(path)
# print(f'the content is {content}')
# for i in content:
#     if '.' not in i:
#         print(f'the content of {i} is {os.listdir(path +"/"+ i)}')

# to run windows / linux commands in the code
# x = os.system('ping 8.8.8.8 -c 4')
# print(x)

# print(f'the current path is {os.getcwd()}')
# os.chdir('..')
# print(f'the current path is {os.getcwd()}')
# os.chdir('../../pre/demo1')
# print(f'the current path is {os.getcwd()}')
# os.mkdir('hodi')pat
# path = f'{os.getcwd()}/hothaifa'
# exist = os.path.exists(path)
# if not exist:
#     os.mkdir('hothaifa')
# else:
#     print('already exists')

# os.rename('hothaifa','rawad')
# content = os.listdir('/Users/hothaifa')
# print(type(os.system('ls')))

# size = os.path.getsize('exercise.py')
# print(f'the size of exercise.py {size} byte')


#    ..    []   []
for path, dirs,files in os.walk('/'):
    for name in dirs:
        print(os.path.join(path,name)) # to print the the files from the root