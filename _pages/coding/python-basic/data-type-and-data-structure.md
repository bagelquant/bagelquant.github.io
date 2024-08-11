---
title: "Data Types and Data Structure"
permalink: /coding/python-basic/data-types-and-data-structure/
sidebar:
  nav: python-basic
---

Coding is all about representing real-world problems in a digital environment. First things to learn in coding are deal with `variables` and `data types`.
- **Variables**: A container that stores data. You can think of it as a box that holds information.
- **Data Types**: The type of data that can be stored in a variable. For example, numbers, text, and lists.
- **Data Structure**: A way to organize and store data in a computer so that it can be used efficiently.

For example: 

- `X = 5`, X is a **variable that stores the number `5`.
- X is an integer **data type**.
- We can store multiple numbers or variables in a list `[1, 2, 3, 4, 5]`. This is a **data structure**.

In this article, we will learn about different data type and data structures in Python. 

> This series of articles is designed for beginners in coding. The methology is to learn by doing. Here just a brief introduction to the concept. We will dive deeper into each concept in the following practical examples.

## Basic Data Types in Python

Python has several built-in data types that are used to store different types of information. Here are some of the basic data types in Python:

- **Integers**: Whole numbers, such as 1, 2, 3, 4, 5.
- **Floats**: Numbers with decimal points, such as 3.14, 2.718.
- **Strings**: Text, such as "Hello, World!".
- **Booleans**: True or False values.

You can use the `type()` function to check the data type of a variable. For example:

```python
x = 5
print(type(x))  # Output: <class 'int'>
```

### Integers and Floats

Integers and floats are used to represent numbers in Python. Integers are whole numbers, while floats are numbers with decimal points. For example:

```python
x = 5  # Integer
y = 3.14  # Float
```

You can perform arithmetic operations on integers and floats, such as addition, subtraction, multiplication, and division. For example:

```python
x = 5
y = 3.14
print(x + y)  # Output: 8.14
print(x - y)  # Output: 1.86
print(x * y)  # Output: 15.7
print(x / y)  # Output: 1.592356687898089
```

> Why separate integers and floats? Integers are faster to process than floats. Therefore, if you are working with whole numbers, use integers to improve performance. The reason is that floats require more memory and processing power to store and manipulate.

### Strings

Strings are used to represent text in Python. You can create strings by enclosing text in single or double quotes. For example:

```python
name = "Alice"
message = 'Hello, World!'
print(name)  # Output: Alice
print(message)  # Output: Hello, World!
```

You can perform various operations on strings, such as concatenation, slicing, and formatting. For example:

```python
name = "Alice"
message = "Hello, " + name
print(message)  # Output: Hello, Alice
```python

You cannot perform arithmetic operations on strings with numbers. For example, the following code will raise an error: 

```python
message = "Hello, " + 5  # Error: can only concatenate str (not "int") to str
```

Use the `str()` function to convert numbers to strings before concatenating them with other strings. For example:

```python
message = "Hello, " + str(5)
print(message)  # Output: Hello, 5
```

> Functions: a block of code that performs a specific task. You can use built-in functions or create your own functions to perform specific tasks. We will cover functions in more detail in a later article.

Samiliar to `str()`, you can use `int()` and `float()` functions to convert strings to integers and floats

#### Selecting Characters and Slicing Strings

You can select individual characters from a string using the index of the character. The index starts at 0 for the first character and increases by 1 for each subsequent character. For example:

```python
message = "Hello, World!"
print(message[0])  # Output: H
print(message[7])  # Output: W

# Slicing strings
print(message[0:5])  # Output: Hello
print(message[7:])  # Output: World!
```

> Reminder: Python uses zero-based indexing. The first element in a list or string has an index of 0, the second element has an index of 1, and so on.

### Booleans

Booleans are used to represent True or False values in Python. Booleans are often used in conditional statements to control the flow of a program. For example:

```python
x = True
y = False
print(x)  # Output: True
print(y)  # Output: False
```

> Notice: `True` and `False` are uppercase in Python. If you use lowercase `true` or `false`, Python will raise an error.

### Variables naming convention

When naming variables, follow these conventions:

- Use descriptive names that reflect the purpose of the variable.
- Use lowercase letters and underscores to separate words in variable names. For example, `first_name`, `last_name`.

> Some bad examples: `a`, `b`, `c`. These names do not provide any information about the purpose of the variable.

> You cannot use reserved keywords as variable names. For example, `if`, `else`, `for`, `while`, `def`, `class`, `import`, `from`, `as`, `return`, `break`, `continue`, `pass`, `global`, `nonlocal`, `lambda`, `try`, `except`, `finally`, `raise`, `assert`, `with`, `yield`, `in`, `is`, `and`, `or`, `not`, `True`, `False`, `None`.

## Data Structures in Python

Data structures are used to organize and store data in a computer so that it can be used efficiently. Python has several built-in data structures that are used to store collections of data. Here are some of the basic data structures in Python:

- **Lists**: Ordered collections of items. For example, `[1, 2, 3, 4, 5]`.
- **Tuples**: Ordered collections of items that cannot be modified. For example, `(1, 2, 3, 4, 5)`.
- **Dictionaries**: Unordered collections of key-value pairs. For example, `{'name': 'Alice', 'age': 30}`.
- **Sets**: Unordered collections of unique items. For example, `{1, 2, 3, 4, 5}`.


You can access individual items in a `iterable` data structure using the index of the item. The index starts at 0 for the first item and increases by 1 for each subsequent item. For example:

```python
# List
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Output: 1
print(numbers[3])  # Output: 4
# Tuple
numbers_tuple = (1, 2, 3, 4, 5)
print(numbers_tuple[0])  # Output: 1
print(numbers_tuple[3])  # Output: 4
```

You can put any data type in a list or tuple. For example, you can have a list of strings, a list of numbers, or a list of lists. For example:

```python
# List of strings
fruits = ["apple", "banana", "cherry"]
# List of numbers
ages = [25, 30, 35]
# List of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# List of mixed data types
mixed = [1, "apple", True, 3.14]
```

### Dictionaries

Dictionaries are used to store key-value pairs in Python. You can access the value associated with a key using the key. For example:

```python
person = {'name': 'Alice', 'age': 30}
print(person['name'])  # Output: Alice
print(person['age'])  # Output: 30
```

## Summary

In this article, we learned about different data types and data structures in Python. We covered:

- Basic data types in Python, such as integers, floats, strings, and booleans.
- How to perform arithmetic operations on integers and floats.
- How to create and manipulate strings in Python.
- How to use booleans to represent True or False values.
- How to select characters and slice strings.
- How to create and access items in lists, tuples, dictionaries, and sets.

We will explore each data type and data structure in more detail in the following articles, especially how to use `iterable` data structures to store and manipulate collections of data.

