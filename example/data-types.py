# ---------------NUMERIC TYPES-------------------------
# print(100)
# print(0b100) #binary
# print(0o100) #octal
# print(0x100) #hexadecimal
# print(type(float(100)))
# print((int(10.56)))
# print(10//3)
# print(bin(24))
# print(type(0b100))

#--------NOTE---------
# print(id(1), id(1))
# i1 = 1
# i2 = 1
# print(id(i1), id(i2))

#-----------------------

# ---------TEXT TYPE----------------------------
# print(type(str(1)) == str)
# print(isinstance(str(0b100), int))
# print('hello' + str(123)) #hello123 
# print('1' * 3) #111
# print('hello'    'hello123') #hellohello123
# print(','.join(['heloo', '1234', 'python'])) #heloo,1234,python
# print('%.3f middle %s %s!' % (12.56, 'python', '1234')) #12.560 middle python 1234!
# print('{1} {2} middle {0} heloo1'.format(1, 123, 'hello')) #123 hello middle 1 heloo1
# s1, s2, s3 = 'Python', 'String', 12
# print(f'{s1} {s2} middle {3*10} {s3*5} {"thinh"} {{thinh}}')
# a = '''a"double"' "''dwd''""
# endline
# '''
# print(a)
# print('0123456789'[3:]) #3456789
# print('0123456789'[-6:-1]) #45678
# str1 = 'thinh'
# str2 = 'thinh'
# print(id(str1), id(str2))


#------SEQUENCE TYPES (list, tuple, range) | MAPPING TYPE (dictionary) | SET TYPES (set, frozenset)--------------------------------
# print(["abc", 34, True, 40, "male"])
# print(type([2]))
# a = [2, 'hello']
# a1 = [2, 'hello']
# b = a
# c = a.copy()
# a.append(1)
# b.extend(['python',12345])
# a.insert(1, 'new')
# print(id(a), id(b), id(c), id(a1))
# print(a,b,c, a1)

# -------NOTE---------------
# dict1 = {'a': 'thinh', 'a': 'hello', 'b': 'hello' , 1: 'thinh', '1': 'thinh', False: range(10)}
# dict2 = {'a': 'thinh', 'a': 'hello', 'b': 'hello' , 1: 'thinh', '1': 'thinh', False: range(10)}
# print(id(({'a': 'thinh', 'a': 'hello', 'b': 'hello' , 1: 'thinh', '1': 'thinh', True: range(10)})))
# print(id(({'a': 'thinh', 'a': 'hello', 'b': 'hello' , 1: 'thinh', '1': 'thinh', True: range(10)})))
# print(id(dict1))
# print(id(dict2))
#---------------------------------------------------------

# print({0, 0, 1, (1,1,5), ((1,1,5),), range(10)})
# print(type(((1,2,3),)))
# print(type((1,2,3)))

#--------------------NOTE--------------
# print(id(([1,2,3], {1,2,3,4,5,12,3}, (1,2,3,4,5,5), {False: 1}))) # same id
# print(id(([1,2,3], {1,2,3,4,5,12,3}, (1,2,3,4,5,5), {False: 1}))) # same id
# tup1 = ([1,2,3], {1,2,3,4,5,12,3}, (1,2,3,4,5,5), {False: 1}) # same id
# tup2 = ([1,2,3], {1,2,3,4,5,12,3}, (1,2,3,4,5,5), {False: 1}) #differnt id
# print(id(tup1), id(tup2))
#----------------------------------------

# print({(1,2,3), range(10), frozenset(range(10))}) # ele in set must be immutable
# print({True: range(10), (1,23): {1,2,3}, frozenset({1,2}): {1: 1}, range(1): (1,2)}) # => key of dict must be immutable

#---------------ORDERED vs UNORDERED---------------------
# letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string_letters = str(letters)
# lists_letters = list(letters)
# tuples_letters = tuple(letters)
# sets_letters = set(letters)


# print("String: ", string_letters)
# print() # for new line
# print("Lists: ", lists_letters)
# print() # for new line
# print("Tuples: ", tuples_letters)
# print() # for new line
# print("Sets: ", sets_letters)

#---------------UNPACK ITEMS IN COLLECTION DATA TYPES------------------------

# l = [1, 2, 3, 4] # unpack list
# l1, l2 ,l3, l4 = l
# (l1, l2, l3, l4) = l
# [l1, l2, l3, l4] = l
# print(l1, l2, l3, l4) # 1 2 3 4

# s = {1, 2, 3, 4} # unpack set
# s1, s2 ,s3, s4 = s
# (s1, s2, s3, s4) = s
# [s1, s2, s3, s4] = s
# print(s1, s2, s3, s4) # 1 2 3 4

# t = (1, 2, 3, 4) # unpack tuple
# t1, t2 ,t3, t4 = t
# (t1, t2, t3, t4) = t
# [t1, t2, t3, t4] = t
# print(t1, t2, t3, t4) # 1 2 3 4

# d = {1: 'one', 2: 'two', 3: 'three', 4: 'four'} # unpack dictionary
# d1, d2 ,d3, d4 = d # d.keys()
# d11, d22, d33, d44 = d.items() # unpack list of keys
# d111, d222, d333, d444 = d.values() # unpack list of values
# (d1, d2, d3, d4) = d
# [d1, d2, d3, d4] = d
# print(d1, d2, d3, d4) # 1 2 3 4 (keys of dict)
# print(d11, d22, d33, d44) # (1, 'one') (2, 'two') (3, 'three') (4, 'four')
# print(d111, d222, d333, d444) # one two three four (values)