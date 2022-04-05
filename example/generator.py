# A simple generator function
def my_gen():
    n = 1
    print("This is printed first")
    yield n  # Generator function contains yield statements

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print("This is printed at last")
    yield n


# # It returns an object but does not start execution immediately.
# a = my_gen()
# print(a)
# print(my_gen())
# print(next(a))
# print(next(a))
# print(next(a))

# for i in my_gen():
#     print(i)
# print(sum(a))
# ---------------------------------------------------------------------
def rev_str_for(my_str):
    length = len(my_str)
    for i in range(length):
        # print(my_str[i])
        yield my_str[i]
        # print(my_str[i])
        # print(i)


def rev_str_while(my_str):
    i = 0
    while i < len(my_str):
        # print(my_str[i])
        yield my_str[i]
        # print(my_str[i])
        # print(i)
        i += 1


# g = rev_str_while("hello")
# print(next(g))
# print(next(g))
# print(next(g))

# for char in rev_str_while("hello"):
#     print(char)

# ---------------------Python Generator Expression-----------------------
# g = (i**2 for i in range(4))  # generator expression
# t = tuple(i**2 for i in range(4))
# l = [i for i in g]  # list expression
# print(g, t, l)
# print(sum(i**2 for i in range(4)))  # use generator expression as function arguments

# -------------------------------------------------------------------
# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2


# even_num = all_even()
# print(next(even_num))
# print(next(even_num))

# ----------------------------------------------------------------------
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num**2


a = fibonacci_numbers(10)
# print([i for i in a])
b = square(a)
# print([i for i in b])
# print(list(map(lambda i: i, b)))
print(sum(b))
