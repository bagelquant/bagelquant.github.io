---
title: Control Flow
permalink: /coding/python-basic/control-flow/
sidebar:
  nav: python-basic
---

Quickly, let's review the basic concepts of coding:

- **Variables**: A container that stores data. You can think of it as a box that holds information.
  - Therefore, a representation of real-world problems in a digital environment.
- **Data Types**: The type of data that can be stored in a variable. For example, numbers, text, and lists.
- **Data Structure**: A way to organize and store data in a computer so that it can be used efficiently.

Now, after we could represent the real-world problems in a digital environment, we need to make decisions based on the data we have. This is where control flow comes in.

## Control Flow

Control flow is the order in which individual statements, instructions, or function calls of an imperative program are executed or evaluated. The control flow of a Python program is regulated by conditional statements, loops, and function calls.

> In short, control flow is the order in which the program's code executes.

There are three main types of control flow in Python:

- **Sequential Control Flow**: The default control flow in Python. The statements are executed line by line in the order they appear in the script.
- **Conditional Control Flow**: The program executes different blocks of code based on the evaluation of a condition.
- **Iterative Control Flow**: The program executes the same block of code multiple times based on the evaluation of a condition.

## Conditional Control Flow

Conditional control flow allows the program to execute different blocks of code based on the evaluation of a condition. Here is an quick example:

```python
x = 5

if x > 0:  # If x is greater than 0, then execute the following block of code
    print("x is positive")
elif x == 0:  # If x is equal to 0, then execute the following block of code
    print("x is zero")
else:  # If x is less than 0, then execute the following block of code
    print("x is negative")
```

Key points:

- **Indentation and code blocks**: In Python, code blocks are defined by indentation. The code block following the `if`, `elif`, or `else` statement must be indented.
- **Colon `:`**: The colon `:` is used to indicate the beginning of a code block.
- **`if`, `elif`, `else`**: These are conditional statements that allow the program to execute different blocks of code based on the evaluation of a condition.

> YOU MUST INDENT THE CODE BLOCKS. Otherwise, you will get an `IndentationError`.

## Iterative Control Flow

Iterative control flow allows the program to execute the same block of code multiple times based on the evaluation of a condition. Here is an quick example:

```python
some_sample_str_list = ["apple", "banana", "cherry"]

for x in some_sample_str_list:
    print(x)
```

Key points:

- **`for` loop**: The `for` loop is used to iterate over a sequence (e.g., a list, tuple, or string).
- **`in` keyword**: The `in` keyword is used to iterate over the elements of a sequence.
- **Indentation and code blocks**: Similar to conditional control flow, the code block following the `for` statement must be indented.


### Break and Continue Statements

- **`break` statement**: The `break` statement is used to exit a loop prematurely. It is often used to stop the loop when a certain condition is met.
- **`continue` statement**: The `continue` statement is used to skip the current iteration of a loop and continue with the next iteration.

We could combine the `if` statement with the `break` and `continue` statements to control the flow of the loop.

```python

sample_str_list = ["apple", "banana", "cherry"]

for x in sample_str_list:
    if x == "banana":  # If x is equal to "banana", then exit the loop
        break
    print(x)
```

In this example, the loop will stop when the value of `x` is `"banana"`.

Remember the sequential control flow is the default control flow in Python. The statements are executed line by line in the order they appear in the script. if we put `print(x)` before the `if` statement, the output will print the list members first then exit the loop when the value of `x` is `"banana"`.

### While Loop

The `while` loop is used to execute a block of code repeatedly as long as a condition is `True`. Here is an example:

```python
i = 1
while i < 6:
    print(i)
    i += 1  # Increment the value of i by 1
```

Key points:

- **`while` loop**: The `while` loop is used to execute a block of code repeatedly as long as a condition is `True`.
- **Indentation and code blocks**: The code block following the `while` statement must be indented.
- **Incrementing the counter**: It is important to increment the counter inside the loop to avoid an infinite loop.

#### Infinite While Loop

An infinite loop is a loop that never stops. The condition of the loop is always `True`. Here is an example of an infinite loop:

```python
i = 1
while True:
    print(i)
    i += 1
```

This operation will continue until you stop the program manually. Usally, we use this kind of loop when we need to run the program continuously. For example, a server that listens to incoming requests, or a GUI application that waits for user input.

## A weather app example

By utilizing the conditional and iterative control flow, we can create a simple weather app.

Let's create a simple weather app that asks the user for the temperature and provides a weather description based on the temperature. Here is the code:

```python
# input() is a function that allows the user to input data
user_input_temperature = input("Enter the temperature: ")

# Convert the user input to a float
temperature = float(user_input_temp)

# Check the temperature and provide a weather description

if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a cold day")
else:
    print("It's a freezing day")
```

Now you can run the code and input the temperature. The program will provide a weather description based on the temperature.

### Add infinite loop to the weather app

To make the weather app run continuously, we can add an infinite loop to the code. And add a condition to exit the loop when the user inputs `q`.

```python
while True:
    # user input
    user_input_temperature = input("Enter the temperature: ")

    # Exit the loop if the user inputs 'q'
    if user_input_temperature == "q":
        break
    
    # Convert the user input to a float
    temperature = float(user_input_temperature)

    if temperature > 30:
        print("It's a hot day")
    elif temperature > 20:
        print("It's a nice day")
    elif temperature > 10:
        print("It's a cold day")
    else:
        print("It's a freezing day")
```

### Robustness improvement

In the above example, if users input a non-numeric value, the program will raise a `ValueError`. We can add an additional `if` statement to check if the user input is a numeric value.

```python

while True:
    # user input
    user_input_temperature = input("Enter the temperature: ")

    # Exit the loop if the user inputs 'q'
    if user_input_temperature == "q":
        break
    
    # Check if the user input is a numeric value
    if not user_input_temperature.isnumeric():  # A function that checks if the string contains only numeric characters
        print("Please enter a numeric value")
        continue  # Skip the current iteration and continue with the next iteration

    # Convert the user input to a float
    temperature = float(user_input_temperature)

    if temperature > 30:
        print("It's a hot day")
    elif temperature > 20:
        print("It's a nice day")
    elif temperature > 10:
        print("It's a cold day")
    else:
        print("It's a freezing day")
```

Now the program will check if the user input is a numeric value. If the user input is not a numeric value, the program will print a message and continue with the next iteration.

## Key Takeaways

- Control flow is the order in which the program's code executes.
- There are three main types of control flow in Python: sequential, conditional, and iterative.
- Conditional control flow allows the program to execute different blocks of code based on the evaluation of a condition.
- Iterative control flow allows the program to execute the same block of code multiple times based on the evaluation of a condition.
- The `break` statement is used to exit a loop prematurely.
- The `continue` statement is used to skip the current iteration of a loop and continue with the next iteration.
- The `while` loop is used to execute a block of code repeatedly as long as a condition is `True`.

