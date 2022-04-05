# class EmptyClass:
#     ...
#     # pass
# e = EmptyClass()
# print(type(e)) # type of e is 'EmptyClass'
# print(type(EmptyClass)) # type of class itself is 'type'


# ______________________________________________________________#

# class A:
#     def __init__(self, bb):
#         self.b = bb
#         print(self, self.b)

# class B():
#     def __init__(self):
#         self.a = A(self)
#         print(self, self.a)
#     def __del__(self):
#         print("die")
# b = B() #die because of circular reference

# ______________________________________________________________#
