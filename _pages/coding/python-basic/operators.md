---
title: "Operators"
permalink: /coding/python-basic/operators/
sidebar:
  nav: python-basic
---

Operators are symbols that perform operations on variables and values. Python has several types of operators, including arithmetic, comparison, logical, assignment, bitwise, and membership operators. In this article, we will cover the basic operators in Python.

Example of operators:

- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators**: `and`, `or`, `not`
- **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
- **Bitwise Operators**: `&`, `|`, `^`, `~`, `<<`, `>>`
- **Membership Operators**: `in`, `not in`

## Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on variables and values. Here are some of the basic arithmetic operators in Python:

- Basic arithmetic operators: `+`, `-`, `*`, `/`
- Floor division: `//`: Returns the integer part of the division
- Modulus: `%`: Returns the remainder of the division
- Exponentiation: `**`: Raises the left operand to the power of the right operand

```python
x = 10
y = 3
print(x + y)  # Output: 13
print(x - y)  # Output: 7
print(x * y)  # Output: 30
print(x / y)  # Output: 3.3333333333333335
print(x // y)  # Output: 3
print(x % y)  # Output: 1
print(x ** y)  # Output: 1000
```

## Comparison Operators

Comparison operators are used to compare two values. They return `True` or `False` based on the comparison. Here are some of the basic comparison operators in Python:

- Equal: `==`
- Not equal: `!=`
- Greater than: `>`
- Less than: `<`
- Greater than or equal to: `>=`
- Less than or equal to: `<=`

```python
x = 10
y = 3
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)  # Output: True
print(x < y)  # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False
```

> Comparison operators are often used in conditional statements to make decisions based on the comparison result. We will see some exaples in the control flow section.

## Logical Operators

Logical operators are used to combine conditional statements. They return `True` or `False` based on the conditions. Here are the basic logical operators in Python:

- `and`: Returns `True` if both statements are true
- `or`: Returns `True` if one of the statements is true
- `not`: Returns `True` if the statement is false

```python
x = 10
y = 3
z = 5
print(x > y and x > z)  # Output: True
print(x > y or x < z)  # Output: True
print(not x > y)  # Output: False
```

> Logical operators are often used to combine multiple conditions in conditional statements. Also commonly used in loops and functions.

## Assignment Operators

Assignment operators are used to assign values to variables. They can also perform arithmetic operations on variables and assign the result to the variable. Here are some of the basic assignment operators in Python:

- `=`: Assigns the value to the variable
- `+=`: Adds the value to the variable and assigns the result to the variable
- `-=`: Subtracts the value from the variable and assigns the result to the variable
- `*=`: Multiplies the variable by the value and assigns the result to the variable
- `/=`: Divides the variable by the value and assigns the result to the variable
- `//=`: Performs floor division on the variable and assigns the result to the variable
- `%=`: Performs modulus on the variable and assigns the result to the variable

```python
x = 10  # Assigns 10 to x
y = 3  # Assigns 3 to y

x += 1  # Adds 1 to x and assigns the result to x
print(x)  # Output: 11 = 10 + 1
x += y  # Adds y to x and assigns the result to x
print(x)  # Output: 14 = 11 + 3

x -= 1  # Subtracts 1 from x and assigns the result to x
print(x)  # Output: 13 = 14 - 1
```

> Assignment operators are often used to update the value of a variable based on the current value of the variable.

## Bitwise Operators

Bitwise operators are used to perform bitwise operations on integers. They treat the operands as binary numbers and perform operations on each bit. Here are some of the basic bitwise operators in Python:

- `&`: Bitwise AND
- `|`: Bitwise OR
- `^`: Bitwise XOR
- `~`: Bitwise NOT
- `<<`: Bitwise left shift
- `>>`: Bitwise right shift

```python
x = 10
y = 3
print(x & y)  # Output: 2
print(x | y)  # Output: 11
print(x ^ y)  # Output: 9
print(~x)  # Output: -11

x = 10
print(x << 1)  # Output: 20
print(x >> 1)  # Output: 5
```

> Bitwise operators are often used in low-level programming, such as device drivers and network programming. We use them less frequently in high-level programming. So, don't worry if you find them confusing.

## Membership Operators

Membership operators are used to test if a sequence is present in an object. They return `True` or `False` based on the membership test. Here are the basic membership operators in Python:

- `in`: Returns `True` if the sequence is present in the object
- `not in`: Returns `True` if the sequence is not present in the object

```python
x = [1, 2, 3, 4, 5]
print(1 in x)  # Output: True
print(6 in x)  # Output: False
print(1 not in x)  # Output: False
print(6 not in x)  # Output: True
```

> Membership operators are often used to check if an element is present in a list, tuple, or dictionary. They are useful in conditional statements and loops.

## Key Takeaways

- Arithmetic operators for mathematical operations
- Comparison operators for comparing values
- Logical operators for combining conditional statements
- Assignment operators for assigning values to variables
- Bitwise operators for performing bitwise operations on integers
- Membership operators for testing if a sequence is present in an object

