# *Python Data Types*

- Text type: *`str`*
- Numeric types: *`int, float, complex`*
- Sequence types: *`list, tuple, range`*
- Mapping type: *`dict`*
- Set types: *`set, frozenset`*
- Boolean type: *`bool`*
- Binary types: *`bytes, bytearray, memoryview`*

---

1. Do Python have primitive data types ?

> Everything in Python is an object, even int or float,... the obj type is just another 'struct' such as int, dict, so pure python does not have primitive datatype.

2. List and Tuple, which one uses more memory and Why?

> Tuple just store the obj types directly whereas list need an extra layer to store an array of pointers, then that array of pointers point to the obj types.
