import datetime
import sys

print('hello')
print('hello')
print(sys.maxsize)  # max integer size
print(sys.executable)
print(sys.platform)
print(sys.version)  # python version
if datetime.datetime.now().hour == 20:
    sys.exit(0)  # terminate the code
print('hello')
print('hello')
