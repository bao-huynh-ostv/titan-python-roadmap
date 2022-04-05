# *Data types*

- **Pure python does not have primitive data types**

> *- Everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.*
>
> *- In the Python standard libraries, there is an array type which implements and supports some primitive types. Also the struct module implements methods for handling a number of primitive data types and formats.*
>
>> *+ Under the hood, ***`str`*** is arrays of bytes representing unicode characters*
>
- **Every object has an identity, a type, and a value**

> - **Identity**
>
>> An object’s identity never changes once it has been created
>>
>> **`id()`** function returns an integer representing identity.
>
> - **Type**
>
>> An object type is unchangeable like the identity
>>
>> **`type()`** function returns the type of an object
>
> - **Value**
>
>> The value of some objects can change
>> Objects whose value **can change** are said to be **mutable**
>>
>> Objects whose value is **unchangeable** once they are created are called **immutable**

## Built-in data types

### - *Numeric types*

> **`int`** , **`float`** , **`complex`**
>

### - *Text type*

> **`str`**
>

### - *Sequence types*

> **`list`** , **`tuple`** , **`range`**
>
> **`list`** and **`tuple`** allow duplicate item

### - *Mapping type*

>
> **`dict`**
>
> Not allow duplicate key
>
>> - **`{key: value1, key: value2, key: value3}`** &rarr; **`{key: value3}`**
>
> *Key of **`dict`** must be immutable data*  
>

### - *Set type*

> **`set`** , **`fronzenset`**
>
> Not allow duplicate item
>
>> **`{value1, value2, value3, value3}`** &rarr; **`{value1, value2, value3}`**
>
> *Each item of **`set`** and **`frozenset`** must be immutable data*  

### - *Boolean type*

> **`bool`**
>

### - *Binary types*

> **`bytes`** , **`bytearray`** , **`memoryview`**
>
----------------------------------------------------

## Mutable and Immutable data types in Python

### - *Mutable data types*

> - **`list`** , **`dict`** , **`set`**
>

### - *Immutable data types*

> - **`tuple`** , **`range`** , **`string`** , **`int`** , **`float`** , **`complex`** , **`bool`** , **`frozenset`**
>