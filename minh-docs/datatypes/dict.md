# DICTIONARIES

Dictionaries and lists share the following characteristics:

- Both are mutable.
- Both are dynamic. They can grow and shrink as needed.
- Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.

Dictionaries differ from lists primarily in how elements are accessed:

- List elements are accessed by their position in the list, via indexing.
- Dictionary elements are accessed via keys.

You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value:
```python
d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}
```

You can also construct a dictionary with the built-in dict() function. The argument to dict() should be a sequence of key-value pairs. A list of tuples works well for this:
```python
d = dict([
    (<key>, <value>),
    (<key>, <value),
      .
      .
      .
    (<key>, <value>)
])
```

If the key values are simple strings, they can be specified as keyword arguments. So here is yet another way to define MLB_team:
```python
>>> MLB_team = dict(
...     Colorado='Rockies',
...     Boston='Red Sox',
...     Minnesota='Twins',
...     Milwaukee='Brewers',
...     Seattle='Mariners'
... )
```

---

## Accessing Dictionary Values

Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:
```python
>>> MLB_team['Kansas City'] = 'Royals'
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners', 'Kansas City': 'Royals'}
```

To delete an entry, use the del statement, specifying the key to delete:
```python
>>> del MLB_team['Seattle']
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Kansas City': 'Royals'}
```

An object of any immutable type can be used as a dictionary key. Accordingly, there is no reason you can’t use integers:
```python
>>> d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
>>> d
{0: 'a', 1: 'b', 2: 'c', 3: 'd'}

>>> d[0]
'a'
>>> d[2]
'c'
```

> ***Note**: Although access to items in a dictionary does not depend on order, Python does guarantee that the order of items in a dictionary is preserved. When displayed, items will appear in the order they were defined, and iteration through the keys will occur in that order as well. Items added to a dictionary are added at the end. If items are deleted, the order of the remaining items is retained.*

---

## Restrictions on Dictionary Keys

There are a couple restrictions that dictionary keys must abide by.

> ***First, a given key can appear in a dictionary only once. Duplicate keys are not allowed.***  

If you specify a key a second time during the initial creation of a dictionary, the second occurrence will override the first:
```python
>>> MLB_team = {
...     'Colorado' : 'Rockies',
...     'Boston'   : 'Red Sox',
...     'Minnesota': 'Timberwolves',
...     'Milwaukee': 'Brewers',
...     'Seattle'  : 'Mariners',
...     'Minnesota': 'Twins'
... }
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}
```

> ***Secondly, a dictionary key must be of a type that is immutable. Several of the immutable types are integer, float, string, and Boolean — have served as dictionary keys.***

A tuple can also be a dictionary key, because tuples are immutable:
```python
>>> d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
>>> d[(1,1)]
'a'
>>> d[(2,1)]
'c'
```
*(Recall from the discussion on tuples that one rationale for using a tuple instead of a list is that there are circumstances where an immutable type is required. This is one of them.)*

However, neither a list nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable:
```python
>>> d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
TypeError: unhashable type: 'list'
```

> **Technical Note**: Why does the error message say “unhashable”?
>
> Technically, it is not quite correct to say an object must be immutable to be used as a dictionary key. More precisely, an object must be hashable, which means it can be passed to a hash function. A hash function takes data of arbitrary size and maps it to a relatively simpler fixed-size value called a hash value (or simply hash), which is used for table lookup and comparison.
>
> Python’s built-in hash() function returns the hash value for an object which is hashable, and raises an exception for an object which isn’t:
> ```python
> >>> hash('foo')
> 11132615637596761
>
> >>> hash([1, 2, 3])
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> TypeError: unhashable type: 'list'
> ```              
> All of the built-in immutable types you have learned about so far are hashable, and the mutable container types (lists and dictionaries) are not. So for present purposes, you can think of hashable and immutable as more or less synonymous.
>
> There are mutable objects which are also hashable.

---

## Restrictions on Dictionary Values

By contrast, there are no restrictions on dictionary values. Literally none at all. A dictionary value can be any type of object Python supports, including mutable types like lists and dictionaries, and user-defined objects.

There is also no restriction against a particular value appearing in a dictionary multiple times:
```python
>>> d = {0: 'a', 1: 'a', 2: 'a', 3: 'a'}
>>> d
{0: 'a', 1: 'a', 2: 'a', 3: 'a'}
>>> d[0] == d[1] == d[2]
True
```

---

## Operators and Built-in Functions

The `in` and `not` in operators return True or False according to whether the specified operand occurs as a key in the dictionary:
```python
>>> MLB_team = {
...     'Colorado' : 'Rockies',
...     'Boston'   : 'Red Sox',
...     'Minnesota': 'Twins',
...     'Milwaukee': 'Brewers',
...     'Seattle'  : 'Mariners'
... }

>>> 'Milwaukee' in MLB_team
True
>>> 'Toronto' in MLB_team
False
>>> 'Toronto' not in MLB_team
True
```

You can use the in operator together with short-circuit evaluation to avoid raising an error when trying to access a key that is not in the dictionary:
```python
>>> MLB_team['Toronto']
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    MLB_team['Toronto']
KeyError: 'Toronto'

>>> 'Toronto' in MLB_team and MLB_team['Toronto']
False
>>> 'Colorado' in MLB_team and MLB_team['Colorado']
'Rockies'
```
In the second case, due to short-circuit evaluation, the expression MLB_team['Toronto'] is not evaluated, so the KeyError exception does not occur.

---

## Built-in Dictionary Methods

As with strings and lists, there are several built-in methods that can be invoked on dictionaries. In fact, in some cases, the list and dictionary methods share the same name.

### ***d.clear()***

> Clears a dictionary

d.clear() empties dictionary d of all key-value pairs:
```python
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}

>>> d.clear()
>>> d
{}
```

### ***d.get(\<key>[, \<default>])***

> Returns the value for a key if it exists in the dictionary.

`d.get(<key>)` searches dictionary `d` for `<key>` and returns the associated value if it is found. If `<key>` is not found, it returns `None`:
```python
>>> d = {'a': 10, 'b': 20, 'c': 30}

>>> print(d.get('b'))
20
>>> print(d.get('z'))
None
```

If <key> is not found and the optional <default> argument is specified, that value is returned instead of None:
```python
>>> print(d.get('z', -1))
-1
```

### ***d.items()***

> Returns a list of key-value pairs in a dictionary.

`d.items()` returns a list of tuples containing the key-value pairs in d. The first item in each tuple is the key, and the second item is the key’s value:
```python
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}

>>> list(d.items())
[('a', 10), ('b', 20), ('c', 30)]
>>> list(d.items())[1][0]
'b'
>>> list(d.items())[1][1]
20
```

### ***d.keys()***

> Returns a list of keys in a dictionary.

`d.keys()` returns a list of all keys in d:
```python
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}

>>> list(d.keys())
['a', 'b', 'c']
```

### ***d.values()***

> Returns a list of values in a dictionary.

d.values() returns a list of all values in d:
```python
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}

>>> list(d.values())
[10, 20, 30]
```

Any duplicate values in d will be returned as many times as they occur:
```python
>>> d = {'a': 10, 'b': 10, 'c': 10}
>>> d
{'a': 10, 'b': 10, 'c': 10}

>>> list(d.values())
[10, 10, 10]
```

> **Technical Note**: The `.items()`, `.keys()`, and `.values()` methods actually return something called a view object. A dictionary view object is more or less like a window on the keys and values. For practical purposes, you can think of these methods as returning lists of the dictionary’s keys and values.

### ***d.pop(\<key>[, \<default>])***

> Removes a key from a dictionary, if it is present, and returns its value.

If `<key>` is present in `d`, `d.pop(<key>)` removes `<key>` and returns its associated value:
```python
>>> d = {'a': 10, 'b': 20, 'c': 30}

>>> d.pop('b')
20
>>> d
{'a': 10, 'c': 30}
```

`d.pop(<key>)` raises a `KeyError` exception if `<key>` is not in `d`:
```python
>>> d = {'a': 10, 'b': 20, 'c': 30}

>>> d.pop('z')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d.pop('z')
KeyError: 'z'
```

If `<key>` is not in `d`, and the optional `<default>` argument is specified, then that value is returned, and no exception is raised:
```python
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d.pop('z', -1)
-1
>>> d
{'a': 10, 'b': 20, 'c': 30}
```

### ***d.popitem()***

> Removes a key-value pair from a dictionary.

`d.popitem()` removes the last key-value pair added from d and returns it as a tuple:
```python
>>> d = {'a': 10, 'b': 20, 'c': 30}

>>> d.popitem()
('c', 30)
>>> d
{'a': 10, 'b': 20}

>>> d.popitem()
('b', 20)
>>> d
{'a': 10}
```

If `d` is empty, `d.popitem()` raises a `KeyError` exception:
```python
>>> d = {}
>>> d.popitem()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d.popitem()
KeyError: 'popitem(): dictionary is empty'
```

### ***d.update(\<obj>)***

> Merges a dictionary with another dictionary or with an iterable of key-value pairs.

If `<obj>` is a dictionary, `d.update(<obj>)` merges the entries from `<obj>` into `d`. For each key in `<obj>`:

1. If the key is not present in `d`, the key-value pair from `<obj>` is added to `d`.
2. If the key is already present in `d`, the corresponding value in `d` for that key is updated to the value from `<obj>`.

Here is an example showing two dictionaries merged together:
```python
>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d2 = {'b': 200, 'd': 400}

>>> d1.update(d2)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}
```

`<obj>` may also be a sequence of key-value pairs, similar to when the `dict()` function is used to define a dictionary. For example, `<obj>` can be specified as a list of tuples:
```python
>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d1.update([('b', 200), ('d', 400)])
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}
```

Or the values to merge can be specified as a list of keyword arguments:
```python
>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d1.update(b=200, d=400)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}
```
