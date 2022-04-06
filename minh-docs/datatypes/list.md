# LIST

The important characteristics:
- Lists are ordered.
- Lists can contain any arbitrary objects.
- List elements can be accessed by index.
- Lists can be nested to arbitrary depth.
- Lists are mutable.
- Lists are dynamic.

---

## List Are Ordered

Lists that have the same elements in a different order are not the same:
```python
>> a = ['foo', 'bar', 'baz', 'qux']
>>> b = ['baz', 'qux', 'bar', 'foo']
>>> a == b
False
>>> a is b
False

>>> [1, 2, 3, 4] == [4, 1, 3, 2]
False
```

---

## List Can Contain Arbitrary Objects

The elements of a list can all be the same type:
```python
a = [2, 4, 6, 8]
```

Or the elements can be of varying types:
```python
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
```

Lists can even contain complex objects, like functions, classes, and modules:
```python
>>> int
<class 'int'>
>>> len
<built-in function len>
>>> def foo():
...     pass
...
>>> foo
<function foo at 0x035B9030>
>>> import math
>>> math
<module 'math' (built-in)>

>>> a = [int, len, foo, math]
>>> a
[<class 'int'>, <built-in function len>, <function foo at 0x02CA2618>,
<module 'math' (built-in)>]
```

A list can contain any number of objects, from zero to as many as your computer’s memory will allow.    
List objects needn’t be unique. A given object can appear in a list multiple times:
```python
a = [1, 2, 3, 1, 2, 3]
```

---

## List Elements Can Be Accessed By Index

A negative list index counts from the end of the list:
!(https://github.com/bao-huynh-ostv/titan-python-roadmap/tree/minh/images/index.jpg)

Slicing also works. If a is a list, the expression a[m:n] returns the portion of a from index m to, but not including, index n:
```python
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> a[2:5]
['baz', 'qux', 'quux']
```

Both positive and negative indices can be specified:
```python
>>> a[-5:-2]
['bar', 'baz', 'qux']
>>> a[1:4]
['bar', 'baz', 'qux']
>>> a[-5:-2] == a[1:4]
True
```

Omitting the first index starts the slice at the beginning of the list, and omitting the second index extends the slice to the end of the list:
```python
>>> a = [1, 2, 3, 4]
>>> a[:3]
[1, 2, 3]
>>> a[1:]
[2, 3, 4]
>>> a[:]
[1, 2, 3, 4]
```

You can specify a stride—either positive or negative:
```python
>>> a = [1, 2, 3, 4]
>>> a[0:4:2]
[1, 3]
>>> a[4:0:-2]
[4, 2]
>>> a[::1]
[1, 2, 3, 4]
>>> a[::-1]     # reversing a list
[4, 3, 2, 1]
```

***The `[:]` syntax works for lists. However, there is an important difference between how this operation works with a list and how it works with a string.***  

If s is a string, s[:] returns a reference to the same object:
```python
>>> a = 'hello'
>>> a[:] is a
True
```

Conversely, if a is a list, a[:] returns a new object that is a copy of a:
```python
>>> a = [1, 2, 3]
>>> a[:] is a
False
```

*It’s not an accident that strings and lists behave so similarly. They are both special cases of a more general object type called an iterable*  

By the way, in each example above, the list is always assigned to a variable before an operation is performed on it. But you can operate on a list literal as well:
```python
>>> [1, 2, 3, 4][2]
3

>>> [1, 2, 3, 4][::-1]
[4, 3, 2, 1]

>>> 3 in [1, 2, 3, 4]
True
```

For that matter, you can do likewise with a string literal:
```python
>>> 'Hello'[::-1]
'olleh'
```

---

## Lists Can Be Nested

A list can contain sublists, which in turn can contain sublists themselves, and so on to arbitrary depth:
```python
>>> x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
```
There is no limit, short of the extent of your computer’s memory, to the depth or complexity with which lists can be nested in this way.  

All the usual syntax regarding indices and slicing applies to sublists as well:
```python
>>> x[1][1][-1]
'ddd'
>>> x[1][1:3]
[['ccc', 'ddd'], 'ee']
>>> x[3][::-1]
['ii', 'hh']
```

---

## Lists Are Mutable