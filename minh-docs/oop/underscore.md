# Underscore in Python

Following are different places where _ is used in Python:

1. Single Underscore:
    - In Interpreter
    - After a name
    - Before a name
2. Double Underscore:
    - `__Double Leading Underscores`
    - `__Double leading and Double trailing underscores__`

## Single Underscore

### In Interpreter

`'_'` returns the value of last executed expression value in Python Prompt/Interpreter
```python
>>> a = 10
>>> b = 10
>>> _
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '_' is not defined
>>> a+b
20
>>> _
20
>>> _ * 2
40
>>> _
40
>>> _ / 2
20
```

### After a name

Python has their by default keywords which we can not use as the variable name. To avoid such conflict between python keyword and variable we use underscore after name
```python
>>> class_ = 1
>>> class_
1
```

### Before a name

Here name prefix by underscore is treated as non-public. If specify `from ... import *` all the name starts with _ will not import. Python does not specify truly private so this ones can be call directly from other modules if it is specified in `__all__`, We also call it `weak Private`

Create python class_file.py:
```python
def public_api():
	print ("public api")

def _private_api():
	print ("private api")
```

Calling file from terminal window:
```python
>>> from class_file import *
>>> public_api()
public api

>>> _private_api()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '_private_api' is not defined

>>> import class_file
>>> class_file.public_api()
public api
>>> class_file._private_api()
private api
```

---

## Double Underscore

### __Double Leading Underscores

Leading double underscore tell python interpreter to rewrite name in order to avoid conflict in subclass. Interpreter changes variable name with class extension and that feature known as the Mangling.

Create testFile.py
```python
class Myclass():
	def __init__(self):
		self.__variable = 10
```

Calling from Interpreter
```python
>>> import testFile
>>> obj = testFile.Myclass()
>>> obj.__variable
Traceback (most recent call last):
File "", line 1, in
AttributeError: Myclass instance has no attribute '__variable'
nce has no attribute 'Myclass'
>>> obj._Myclass__variable
10
```

In Mangling python interpreter modify variable name with ___. So Multiple time It use as the Private member because another class can not access that variable directly. Main purpose for __ is to use variable/method in class only If you want to use it outside of the class you can make public api
```python
class Myclass():
	def __init__(self):
		self.__variable = 10
	def func(self)
		print (self.__variable)
```
```python
>>> import testFile
>>> obj = testFile.Myclass()
>>> obj.func()
10
```

Python provides these methods to use it as the operator overloading depending on the user.

Python provides this convention to differentiate between the user-defined function with the module’s function
```python
class Myclass():
	def __add__(self,a,b):
		print (a*b)
```
```python
>>> import testFile
>>> obj = testFile.Myclass()
>>> obj.__add__(1,2)
2
>>> obj.__add__(5,2)
10
```

### `__Double leading and Double trailing underscores__`

Name with start with `__` and ends with same considers special methods in Python. Python provides these methods to use it as the operator overloading depending on the user.

Python provides this convention to differentiate between the user-defined function with the module’s function
```python
class Myclass():
    def __add__(self,a,b):
        print (a*b)
```
```python
>>> import testFile
>>> obj = testFile.Myclass()
>>> obj.__add__(1,2)
2
>>> obj.__add__(5,2)
10
```

---

## Private Methods

In Python, private methods are methods that cannot be accessed outside the class that it is declared in nor to any other base class. In Python, there is no existence of Private methods that cannot be accessed except inside a class. However, to define a private method prefix the member name with double underscore “__”.
```python
# Python program to
# demonstrate private methods

# Creating a Base class
class Base:

	# Declaring public method
	def fun(self):
		print("Public method")

	# Declaring private method
	def __fun(self):
		print("Private method")

# Creating a derived class
class Derived(Base):
	def __init__(self):
		
		# Calling constructor of
		# Base class
		Base.__init__(self)
		
	def call_public(self):
		
		# Calling public method of base class
		print("\nInside derived class")
		self.fun()
		
	def call_private(self):
		
		# Calling private method of base class
		self.__fun()

# Driver code
obj1 = Base()

# Calling public method
obj1.fun()

obj2 = Derived()
obj2.call_public()

# Uncommenting obj1.__fun() will
# raise an AttributeError

# Uncommenting obj2.call_private()
# will also raise an AttributeError
```
```python
Public method

Inside derived class
Public method

Traceback (most recent call last):
  File "/home/09d6f91fdb63d16200e172c7a925dd7f.py", line 43, in 
    obj1.__fun() 
AttributeError: 'Base' object has no attribute '__fun'

Traceback (most recent call last):
  File "/home/0d5506bab8f06cb7c842501d9704557b.py", line 46, in 
    obj2.call_private() 
  File "/home/0d5506bab8f06cb7c842501d9704557b.py", line 32, in call_private
    self.__fun()
AttributeError: 'Derived' object has no attribute '_Derived__fun'
```

The above example shows that private methods of the class can neither be accessed outside the class nor by any base class. However, private methods can be accessed by calling the private methods via public methods.
```python
# Python program to
# demonstrate private methods

# Creating a class
class A:

	# Declaring public method
	def fun(self):
		print("Public method")

	# Declaring private method
	def __fun(self):
		print("Private method")
	
	# Calling private method via
	# another method
	def Help(self):
		self.fun()
		self.__fun()
		
# Driver's code
obj = A()
obj.Help()
```
```python
Public method
Private method
```

### Name mangling

Python provides a magic wand which can be used to call private methods outside the class also, it is known as name mangling. It means that any identifier of the form `__geek` (at least two leading underscores or at most one trailing underscore) is replaced with `_classname__geek`, where classname is the current class name with leading underscore(s) stripped.
```python
# Python program to
# demonstrate private methods
	
# Creating a class
class A:
	
	# Declaring public method
	def fun(self):
		print("Public method")
	
	# Declaring private method
	def __fun(self):
		print("Private method")
		
# Driver's code
obj = A()

# Calling the private member
# through name mangling
obj._A__fun()
```
```python
Private method
```

