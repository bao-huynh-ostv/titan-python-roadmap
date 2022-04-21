# Decorators

By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

## Functions

### First-Class Objects

In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on).

### Inner Functions

It’s possible to define functions inside other functions. Such functions are called inner functions. Here’s an example of a function with two inner functions:
```python
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
```

Whenever you call `parent()`, the inner functions `first_child()` and `second_child()` are also called. But because of their local scope, they aren’t available outside of the `parent()` function.

### Returning Functions From Functions

Python also allows you to use functions as return values. The following example returns one of the inner functions from the outer `parent()` function:
```python
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
```

Note that you are returning first_child without the parentheses. Recall that this means that you are returning a reference to the function `first_child`. In contrast `first_child()` with parentheses refers to the result of evaluating the function. This can be seen in the following example:
```python
>>> first = parent(1)
>>> second = parent(2)

>>> first
<function parent.<locals>.first_child at 0x7f599f1e2e18>

>>> second
<function parent.<locals>.second_child at 0x7f599dad5268>
```

You can now use first and second as if they are regular functions, even though the functions they point to can’t be accessed directly:
```python
>>> first()
'Hi, I am Emma'

>>> second()
'Call me Liam'
```

---

## Simple Decorators

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
```
```python
>>> say_whee()
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```

In effect, the name say_whee now points to the `wrapper()` inner function. Remember that you return wrapper as a function when you call `my_decorator(say_whee)`:
```python
>>> say_whee
<function my_decorator.<locals>.wrapper at 0x7f3c5dfd42f0>
```

Put simply: **decorators wrap a function, modifying its behavior.**

### Syntactic Sugar!

Python allows you to use decorators in a simpler way with the `@` symbol, sometimes called the “pie” syntax. The following example does the exact same thing as the first decorator example:
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

So, `@my_decorator` is just an easier way of saying `say_whee = my_decorator(say_whee)`. It’s how you apply a decorator to a function.

### Reusing Decorators

Create a file called `decorators.py` with the following content:
```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
```

You can now use this new decorator in other files by doing a regular `import`:
```python
from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")
```

### Decorating Functions With Arguments

```python
from decorators import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")
```

Unfortunately, running this code raises an error:
```python
>>> greet("World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given
```

The solution is to use `*args` and `**kwargs` in the inner wrapper function. Then it will accept an arbitrary number of positional and keyword arguments. Rewrite `decorators.py` as follows:
```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
```

### Returning Values From Decorated Functions

What happens to the return value of decorated functions? Well, that’s up to the decorator to decide. Let’s say you decorate a simple function as follows:
```python
from decorators import do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"
```

Try to use it
```python
>>> hi_adam = return_greeting("Adam")
Creating greeting
Creating greeting
>>> print(hi_adam)
None        # Not good
```

Because the `do_twice_wrapper()` doesn’t explicitly return a value, the call `return_greeting("Adam")` ended up returning `None`.

To fix this, you need to **make sure the wrapper function returns the return value of the decorated function**. Change your `decorators.py` file:
```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)    # return values of function
    return wrapper_do_twice
```

### Who Are You, Really?

Introspection is the ability of an object to know about its own attributes at runtime. For instance, a function knows its own name and documentation:
```python
>>> print
<built-in function print>

>>> print.__name__
'print'

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    <full help message>
```

However, after being decorated, `say_whee()` has gotten very confused about its identity. It now reports being the `wrapper_do_twice()` inner function inside the `do_twice()` decorator. Although technically true, this is not very useful information.

To fix this, decorators should use the `@functools.wraps` decorator, which will preserve information about the original function. Update `decorators.py` again:
```python
import functools

def do_twice(func):
    @functools.wraps(func)      # use this
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

You do not need to change anything about the `decorated say_whee()` function:
```python
>>> say_whee
<function say_whee at 0x7ff79a60f2f0>

>>> say_whee.__name__
'say_whee'

>>> help(say_whee)
Help on function say_whee in module whee:

say_whee()
```

> **Technical Detail**: The `@functools.wraps` decorator uses the function functools.`update_wrapper()` to update special attributes like `__name__` and `__doc__` that are used in the introspection.

---

## A Few Real World Examples

This formula is a good boilerplate template for building more complex decorators.
```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

### Timing Functions

Let’s start by creating a `@timer` decorator. It will measure the time a function takes to execute and print the duration to the console. Here’s the code:
```python
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
```

### Debugging Code

The following `@debug` decorator will print the arguments a function is called with as well as its return value every time the function is called:
```python
import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug
```

The signature is created by joining the string representations of all the arguments. The numbers in the following list correspond to the numbered comments in the code:

1. Create a list of the positional arguments. Use `repr()` to get a nice string representing each argument.
2. Create a list of the keyword arguments. The f-string formats each argument as `key=value` where the `!r` specifier means that `repr()` is used to represent the value.
3. The lists of positional and keyword arguments is joined together to one signature string with each argument separated by a comma.
4. The return value is printed after the function is executed.

Let’s see how the decorator works in practice by applying it to a simple function with one position and one keyword argument:
```python
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
```

Note how the `@debug` decorator prints the signature and return value of the `make_greeting()` function:
```python
>>> make_greeting("Benjamin")
Calling make_greeting('Benjamin')
'make_greeting' returned 'Howdy Benjamin!'
'Howdy Benjamin!'

>>> make_greeting("Richard", age=112)
Calling make_greeting('Richard', age=112)
'make_greeting' returned 'Whoa Richard! 112 already, you are growing up!'
'Whoa Richard! 112 already, you are growing up!'

>>> make_greeting(name="Dorrisile", age=116)
Calling make_greeting(name='Dorrisile', age=116)
'make_greeting' returned 'Whoa Dorrisile! 116 already, you are growing up!'
'Whoa Dorrisile! 116 already, you are growing up!'
```

This example might not seem immediately useful since the `@debug` decorator just repeats what you just wrote. It’s more powerful when applied to small convenience functions that you don’t call directly yourself.

The following example calculates an approximation to the mathematical constant e. This example also shows how you can apply a decorator to a function that has already been defined:
```python
import math
from decorators import debug

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))
```

When calling the `approximate_e()` function, you can see the `@debug` decorator at work:
```python
>>> approximate_e(5)
Calling factorial(0)
'factorial' returned 1
Calling factorial(1)
'factorial' returned 1
Calling factorial(2)
'factorial' returned 2
Calling factorial(3)
'factorial' returned 6
Calling factorial(4)
'factorial' returned 24
2.708333333333333
```

### Slowing Down Code

```python
import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)                           # sleep 1s
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
```

### Registering Plugins

Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in architecture:
```python
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
```

The `@register` decorator simply stores a reference to the decorated function in the global `PLUGINS` dict. Note that you do not have to write an inner function or use `@functools.wraps` in this example because you are returning the original function unmodified.

The `randomly_greet()` function randomly chooses one of the registered functions to use. Note that the `PLUGINS` dictionary already contains references to each function object that is registered as a plugin:
```python
>>> PLUGINS
{'say_hello': <function say_hello at 0x7f768eae6730>,
 'be_awesome': <function be_awesome at 0x7f768eae67b8>}

>>> randomly_greet("Alice")
Using 'say_hello'
'Hello Alice'
```

The main benefit of this simple plugin architecture is that you do not need to maintain a list of which plugins exist. That list is created when the plugins register themselves. This makes it trivial to add a new plugin: just define the function and decorate it with `@register`.

---

## Fancy Decorators

https://realpython.com/primer-on-python-decorators/#fancy-decorators