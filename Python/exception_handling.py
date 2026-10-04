
x = 'a'

try:
    if x > 3:
        print('large')
except TypeError as error:
    print('something went wrong',error)


try:
    total = 10//0
    print(total)
except Exception as error:
    print(f'Error: {error}')