import time


def timer(f):
    def wrapper():
        start = time.time()
        f()
        end = time.time() - start
        print(f'Time to run the function: {end}')
    return wrapper

def validator(f):
    def check_age():
        
        age = input('Age: ')

        if int(age) >= 18:
            print('legal age!')
            f()
        else:
            print('not legal age!')
    return check_age


@timer
@validator
def hello_world():
    print('Hello World!')

hello_world()