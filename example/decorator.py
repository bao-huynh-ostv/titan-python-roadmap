import time
from typing import Optional, Union

# ---------------------timer--------------------


def timer(func):
    def inner1(*args, **kwargs):

        begin = time.time()

        func(*args, **kwargs)

        end = time.time()
        
        print(end - begin)

    return inner1


# timer(func)
@timer
def func(num):
    print(num)


# func(10)


# -------------------------validation----------------------------------------------------------------
def validate_data(data_type):
    def inner(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg,data_type):
                    raise Exception("Invalid data type")
            print('pass validate')
            func(*args, **kwargs)
        return wrapper
    return inner
                

# @validate_data(str)
@timer
def func(*args, **kwargs):
    pass

validate_data(str)(func)('thinh', '')
# print(func('thinh', 'thinh123'))
