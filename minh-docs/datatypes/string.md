# STRINGS
Strings in python are surrounded by either single quotation marks or double quotation marks. Ex: `'hello' or "hello"`
## Assign String to a Variable
```python
a = "Hello"
print(a)
```
---
## Multi-line Strings
User three single ''' or double """quotes:
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
---
## Strings are Arrays
Strings in Python are **arrays of bytes** representing unicode of characters.  
However, Python does not have a character data type, a single character is a string with a length of 1.  
Square brackets [] can be used to access elements of the string.
```python
a = "Hello world!"
print(a[1])
```
---
## Looping through a String
Since strings are arrays, we can loop through the characters in a string, with a **`for`** loop
```python
for x in "banana":
    print(x)
```
---
## String length
Use **`len()`** function:
```python
a = "Hello, World!"
print(len(a))
```
---
## Check String
Check if "free" is in the following text:
```python
txt = "The best things in life are free!"
print("free" in txt)
```
or
```python
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
```
---
## Remove whitespace
The strip() method removes any whitespace from the beginning or the end:
```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```
---
## Split String
The split() method splits the string into substrings if it finds instances of the separator:
```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```
---
## String Format
Use the **`format()`** method to insert numbers into strings:
```python
quantity = 3
itemno = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, itemno, price))
```
---
## Escape Character
You will get an error if you use double quotes inside a string that is surrounded by double quotes:
```python
txt = "We are the so-called "Vikings" from the north."
```
To fix this problem, use the escape character   ":
```python
txt = "We are the so-called   "Vikings  " from the north."
```
---
## String is immutable
An immutable object is one that, once created, will not change in its lifetime.
```python
name_1 = "Varun"
name_1[0] = 'T'
```
Output
```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
---
### Solution
One possible solution is to create a new string object with necessary modifications:
```python
name_1 = "Varun"
name_2 = "T" + name_1[1:]
print("name_1 = ", name_1, "and name_2 = ", name_2)
```
Output
```python
name_1 = Varun and name_2 = Tarun
```
To identify that they are different strings, check with the `id()` function:
```python
name_1 = "Varun"
name_2 = "T" + name_1[1:]
print("id of name_1 = ", id(name_1))
print("id of name_2 = ", id(name_2))
```
Output
```python
id of name_1 =  139622734039280
id of name_2 =  139622734040008
```
To understand more about the concept of string immutability, consider the following code:
```python
name_1 = "Varun"
name_2 = "Varun"
print("id of name_1 = ", id(name_1))
print("id of name_2 = ", id(name_2))
```
Output
```python
id of name_1 =  140125413939552
id of name_2 =  140125413939552
```
To dig deeper, execute the following statements:
```python
name_1 = "Varun"
print("id of name_1 = ", id(name_1))

name_1 = "Tarun"
print("id of name_1 afer initialing with new value = ", id(name_1))
```
Output
```python
id of name_1 =  140192230340848
id of name_1 afer initialing with new value =  140192230341520
```
As can be seen in the above example, when a string reference is reinitialized with a new value, it is creating a new object rather than overwriting the previous value.  
In Python, strings are made immutable so that programmers cannot alter the contents of the object (even by mistake). This avoids unnecessary bugs.