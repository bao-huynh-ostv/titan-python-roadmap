# LAMBDA

Detail article, visit: https://realpython.com/python-lambda/

For basic, a lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

## Syntax

```python
lambda arguments : expression
```

Add 10 to argument a, and return the result:
```python
>>> x = lambda a: a + 1
>>> x(1)
2
```

Lambda functions can take any number of arguments:
```python
>>> x = lambda a, b: a * b
>>> x(3, 2)
6
```

## Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.