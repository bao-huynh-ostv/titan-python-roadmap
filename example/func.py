# ------ isinstance() -------
# print(isinstance(5, int)) # => True
# print(type(5) is int) # => True

# print(isinstance("Hello", (float, int, str, list, dict, tuple))) # => True
# print(type('hello') in (float, int, str, list, dict, tuple)) # => True

# class myObj:
#       name = "John"
# y = myObj()
# print(isinstance(y, myObj)) # => True
# print(type(y) is myObj) # => True

# -------------------list | dict | set | tuple comprehension--------------------------------
# l = [i for i in range(1, 10)]
# l1 = [i for i in l if i % 2 == 0 and i > 2]
# print(l1)
# f = lambda i: i // 2
# l11 = list(map(f, l))
# print(l11)
# l3 = [
#     {i for i in l if i % 2 == 0} if i % 2 == 0 else tuple(i for i in l if i % 2 != 0)
#     for i in range(2)
# ]
# d1 = {k: v for k, v in enumerate(l1, 9) if k % 2 != 0}
# print(d1)

# ----------------------global | local | nonlocal variable ------------------------
# def func():
#     global g
#     l = "local"
#     g = g + " 1"
#     print(g)
#     print(l)


# g = "global"
# func()


# def outer():
#     x = "local"
#     print(g)

#     def inner():
#         global g
#         nonlocal x
#         print(x)
#         g = g + " 1"
#         x = "nonlocal"
#         print("inner:", x)

#     inner()
#     print("outer:", x)
#     print("global:", g)


# outer()

# g = globals()
# kaka = 30
# print(id(kaka))
# print(locals())


def modify():
    global kaka
    kaka = 10
    l = locals()
    print(id(kaka))
    # g["kaka"] = 100
    print(l)

    def modify_kaka():
        # nonlocal kaka
        # print(kaka)
        print(id(kaka))
        print(kaka)
        # kaka = 20
        # print(1, kaka)

    modify_kaka()
    print(2, kaka)
    return modify_kaka


modify()
print(kaka)
