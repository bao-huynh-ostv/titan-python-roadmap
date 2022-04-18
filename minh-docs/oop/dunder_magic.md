# Dunder or magic methods in Python

Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting. Few examples for magic methods are: `__init__`, `__add__`, `__len__`, `__repr__` etc.

The `__init__` method for initialization is invoked without any call, when an instance of a class is created, like constructors in certain other programming languages such as C++, Java, C#, PHP etc:
```python
# declare our own string class
class String:
	
	# magic method to initiate object
	def __init__(self, string):
		self.string = string
		
# Driver Code
if __name__ == '__main__':
	
	# object creation
	string1 = String('Hello')

	# print object location
	print(string1)
```

Output
```python
<__main__.String object at 0x7fe992215390>
```

## Overloading Built-in Functions

### Giving a Length to Your Objects Using `len()`

To change the behavior of `len()`, you need to define the `__len__()` special method in your class. Whenever you pass an object of your class to `len()`, your custom definition of `__len__()` will be used to obtain the result.
```python
>>> class Order:
...     def __init__(self, cart, customer):
...         self.cart = list(cart)
...         self.customer = customer
...
...     def __len__(self):
...         return len(self.cart)
...
>>> order = Order(['banana', 'apple', 'mango'], 'Real Python')
>>> len(order)
3
```

When you don’t have the `__len__()` method defined but still call `len()` on your object, you get a `TypeError`:
```python
>>> class Order:
...     def __init__(self, cart, customer):
...         self.cart = list(cart)
...         self.customer = customer
...
>>> order = Order(['banana', 'apple', 'mango'], 'Real Python')
>>> len(order)  # Calling len when no __len__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'Order' has no len()
```

### Making Your Objects Work with abs()

In a class representing a vector in a two-dimensional space, `abs()` can be used to get the length of the vector. Let’s see it in action:
```python
>>> class Vector:
...     def __init__(self, x_comp, y_comp):
...         self.x_comp = x_comp
...         self.y_comp = y_comp
...
...     def __abs__(self):
...         return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5
...
>>> vector = Vector(3, 4)
>>> abs(vector)
5.0
```

### Printing Your Objects Prettily Using `str()`

The `str()` built-in is used to cast an instance of a class to a str object, or more appropriately, to obtain a user-friendly string representation of the object which can be read by a normal user rather than the programmer. You can define the string format your object should be displayed in when passed to `str()` by defining the `__str__()` method in your class. Moreover, `__str__()` is the method that is used by Python when you call `print()` on your object.
```python
>>> class Vector:
...     def __init__(self, x_comp, y_comp):
...         self.x_comp = x_comp
...         self.y_comp = y_comp
...
...     def __str__(self):
...         # By default, sign of +ve number is not displayed
...         # Using `+`, sign is always displayed
...         return f'{self.x_comp}i{self.y_comp:+}j'
...
>>> vector = Vector(3, 4)
>>> str(vector)
'3i+4j'
>>> print(vector)
3i+4j
```

### Representing Your Objects Using `repr()`

The `repr()` built-in is used to obtain the parsable string representation of an object. If an object is parsable, that means that Python should be able to recreate the object from the representation when repr is used in conjunction with functions like `eval()`. To define the behavior of `repr()`, you can use the `__repr__()` special method.

This is also the method Python uses to display the object in a REPL session. If the `__repr__()` method is not defined, you will get something like `<__main__.Vector object at 0x...>` trying to look at the object in the REPL session. Let’s see it in action in the Vector class:
```python
>>> class Vector:
...     def __init__(self, x_comp, y_comp):
...         self.x_comp = x_comp
...         self.y_comp = y_comp
...
...     def __repr__(self):
...         return f'Vector({self.x_comp}, {self.y_comp})'
...

>>> vector = Vector(3, 4)
>>> repr(vector)
'Vector(3, 4)'

>>> b = eval(repr(vector))
>>> type(b), b.x_comp, b.y_comp
(__main__.Vector, 3, 4)

>>> vector  # Looking at object; __repr__ used
'Vector(3, 4)'
```

### Making Your Objects Truthy or Falsey Using `bool()`

The bool() built-in can be used to obtain the truth value of an object. To define its behavior, you can use the `__bool__()` (`__nonzero__()` in Python 2.x) special method.

The behavior defined here will determine the truth value of an instance in all contexts that require obtaining a truth value such as in if statements.

As an example, for the Order class that was defined above, an instance can be considered to be truthy if the length of the cart list is non-zero. This can be used to check whether an order should be processed or not:
```python
>>> class Order:
...     def __init__(self, cart, customer):
...         self.cart = list(cart)
...         self.customer = customer
...
...     def __bool__(self):
...         return len(self.cart) > 0
...
>>> order1 = Order(['banana', 'apple', 'mango'], 'Real Python')
>>> order2 = Order([], 'Python')

>>> bool(order1)
True
>>> bool(order2)
False
```

---

## Overloading Built-in Operators

### Making Your Objects Capable of Being Added Using `+`

The special method corresponding to the `+` operator is the `__add__()` method. Adding a custom definition of `__add__()` changes the behavior of the operator. It is recommended that `__add__()` returns a new instance of the class instead of modifying the calling instance itself. You’ll see this behavior quite commonly in Python:
```python
>>> class Order:
...     def __init__(self, cart, customer):
...         self.cart = list(cart)
...         self.customer = customer
...
...     def __add__(self, other):
...         new_cart = self.cart.copy()			# Recommend
...         new_cart.append(other)
...         return Order(new_cart, self.customer)
...
>>> order = Order(['banana', 'apple'], 'Real Python')

>>> (order + 'orange').cart  # New Order instance
['banana', 'apple', 'orange']
>>> order.cart  # Original instance unchanged
['banana', 'apple']

>>> order = order + 'mango'  # Changing the original instance
>>> order.cart
['banana', 'apple', 'mango']
```

Similarly, you have the `__sub__()`, `__mul__()`, and other special methods which define the behavior of `-`, `*`, and so on. These methods should return a new instance of the class as well.

### Shortcuts: the `+=` Operator

The `+=` operator stands as a shortcut to the expression `obj1 = obj1 + obj2`. The special method corresponding to it is `__iadd__()`. The `__iadd__()` method should make changes directly to the self argument and return the result, which may or may not be self. This behavior is quite different from `__add__()` since the latter creates a new object and returns that, as you saw above.
```python
>>> class Order:
...     def __init__(self, cart, customer):
...         self.cart = list(cart)
...         self.customer = customer
...
...     def __iadd__(self, other):
...         self.cart.append(other)
...         return self		# always remember this
...
>>> order = Order(['banana', 'apple'], 'Real Python')
>>> order += 'mango'
>>> order.cart
['banana', 'apple', 'mango']
```

Similar to `__iadd__()`, you have `__isub__()`, `__imul__()`, `__idiv__()` and other special methods which define the behavior of `-=`, `*=`, `/=`, and others alike.

> **Note**: When `__iadd__()` or its friends are missing from your class definition but you still use their operators on your objects, Python uses `__add__()` and its friends to get the result of the operation and assigns that to the calling instance. Generally speaking, it is safe to not implement `__iadd__()` and its friends in your classes as long as `__add__()` and its friends work properly (return something which is the result of the operation).

### Indexing and Slicing Your Objects Using `[]`

The `[]` operator is called the indexing operator and is used in various contexts in Python such as getting the value at an index in sequences, getting the value associated with a key in dictionaries, or obtaining a part of a sequence through slicing. You can change its behavior using the `__getitem__()` special method.
```python
>>> class Order:
...     def __init__(self, cart, customer):
...         self.cart = list(cart)
...         self.customer = customer
...
...     def __getitem__(self, key):
...         return self.cart[key]
...
>>> order = Order(['banana', 'apple'], 'Real Python')
>>> order[0]
'banana'
>>> order[-1]
'apple'
```

### Reverse Operators: Making Your Classes Mathematically Correct

While defining the `__add__()`, `__sub__()`, `__mul__()`, and similar special methods allows you to use the operators when your class instance is the left-hand side operand, the operator will not work if the class instance is the right-hand side operand:
```python
>>> class Mock:
...     def __init__(self, num):
...         self.num = num
...     def __add__(self, other):
...         return Mock(self.num + other)
...
>>> mock = Mock(5)
>>> mock = mock + 6
>>> mock.num
11

>>> mock = 6 + Mock(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'Mock'
```

To help you make your classes mathematically correct, Python provides you with reverse special methods such as `__radd__()`, `__rsub__()`, `__rmul__()`, and so on.
```python
>>> class Order:
...     def __init__(self, cart, customer):
...         self.cart = list(cart)
...         self.customer = customer
...
...     def __add__(self, other):
...         new_cart = self.cart.copy()
...         new_cart.append(other)
...         return Order(new_cart, self.customer)
...
...     def __radd__(self, other):
...         new_cart = self.cart.copy()
...         new_cart.insert(0, other)
...         return Order(new_cart, self.customer)
...
>>> order = Order(['banana', 'apple'], 'Real Python')

>>> order = order + 'orange'
>>> order.cart
['banana', 'apple', 'orange']

>>> order = 'mango' + order
>>> order.cart
['mango', 'banana', 'apple', 'orange']
```