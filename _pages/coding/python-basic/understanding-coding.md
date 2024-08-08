---
title: "Understanding Coding"
permalink: /coding/python-basic/understanding-coding/
sidebar:
  nav: python-basic
---

## How does computer actually work?

To understand coding, we need to understand how computers work. 

Here is a simple explanation of how a computer represents information:

1. **Binary**: Electricity is either on or off. This is represented as 1 or 0 in binary code.
2. **Translate**: Human pre-defined instructions can relate binary code to specific term.

Example:

- `00000001` can be translated to `A`
- `00000010` can be translated to `B`
- `00000011` can be translated to `C`

> **Note**: The above example is a simple representation. In reality, the binary code is more complex and can represent more than just letters.

The most important takeaway is that computers can only understand binary code. Therefore, human need layers of "translation" to communicate with computers.

## High-level vs Low-level languages

Among many translation layers, some languages are closer to binary code, while others are closer to human language.

- **High-level languages**: Closer to human language. Examples include Python, Java, and C++.
  - **Pros**: Easier to read and write.
  - **Cons**: Slower to execute.
- **Low-level languages**: Closer to binary code. Examples include Assembly and Machine code.

> **Note**: The closer a language is to binary code, the faster it is to execute. However, it $is faster than Python, but it is harder to write and understand. For example, C++ is faster than Python, but it is harder to write and understand.

## Coding language, compiler, and interpreter

Now we know that coding languages just a set of human-readable instructions, it is just plain text. We need a "Translator" to convert these instructions to binary code.

- **Compiler**: Translates the entire code into binary code before execution. Examples include C++ and Java.
- **Interpreter**: Translates the code line by line during execution. Examples include Python and JavaScript.

> **Note**: The difference between compiler and interpreter is that the compiler translates the entire code before execution, while the interpreter translates the code line by line during execution.

## Coding process

The coding process can be broken down into the following steps:

1. **Write code**: Write human-readable instructions in a coding language.
2. **Compile**: Translate the code into binary code. (For compiled languages only)
3. **Execute**: Run the binary code on the computer.
4. **Debug**: Identify and fix errors in the code.

## Wrap up in Python

- It is a high-level language, closer to human language.
  - Therefore, it is easier to read and write.
  - But slower to execute compared to low-level languages.
- Python code just plain text.
  - Need a Python interpreter to translate the code into binary code.
  - Stored in `.py` files.
- It is an interpreted language.
  - Meaning the translation happens during execution.
  - Do not need to compile the code before execution.

