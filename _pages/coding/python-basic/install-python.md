---
title: "Install Python"
permalink: /coding/python-basic/install-python/
sidebar:
  nav: python-basic
---

Now we understand how computers work and how coding languages work. Let's install Python on your computer. Remember, Python is a high-level language, which means it is closer to human language. Therefore, it is easier to read and write. However, it is slower to execute compared to low-level languages.

- **Python Script**: Just a plain text file with `.py` extension. You do not need to download any software to write Python scripts.
- **Python Interpreter**: A program that translates Python scripts into binary code. You need to download Python to run Python scripts.
- **IDE**, **Code Editor**: Software that helps you write and run Python scripts. You can use any text editor, but IDEs and code editors provide more features. -> More on this later.
- **Terminal**: A command-line interface where you can run Python scripts and interact with the computer. Much quicker than using a graphical interface. -> More on this later.

> Install Python is mainly about **Python Interpreter**. You can write Python scripts in any text editor, but you need Python to run them.

This article will guide you through the installation process of Python on your computer using conda environment. 

## What is Environment?

Sometimes, you need to use different versions of Python or different packages for different projects. For example, you may need Python 3.7 for one project and Python 3.8 for another project. 

To manage different versions of Python and packages, you can create different environments. Each environment is like a separate room where you can install different versions of Python and packages.

Conda is a popular package manager that allows you to create and manage different environments.

The process of using `conda` to install Python is as follows:

1. **Create a new environment**: Create a new environment for Python.
2. **Activate the environment**: Activate the environment to use Python.
3. **Install Python in the environment**: Install Python in the environment.

## Install Miniconda

### What is conda?

`conda` is a package manager that allows you to create and manage different environments. It is widely used in the Python community to manage different versions of Python and packages.

However, `conda` is not installed by default when you install Python. You need to install `conda` separately.

There are two popular versions of `conda`:

- **Miniconda**: A minimal version of `conda` that only includes `conda` and Python. You can install other packages as needed.
  - Pros: Smaller download size. You can install only the packages you need.
  - Cons: You need to install other packages manually.
- **Anaconda**: A full version of `conda` that includes `conda`, Python, and many other packages. It is a larger download compared to Miniconda.
  - Pros: Includes many packages out of the box.
  - Cons: Larger download size. You may not need all the packages included. 

> We recommend using Miniconda for beginners. You can install other packages as needed. And you could understand how `conda` works better, and get familiar with the terminal.

### Download Miniconda

1. Go to the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html).
2. Download the installer for your operating system (Windows, macOS, Linux).
3. Run the installer and follow the instructions.

> You need to initialize `conda` in your terminal. You can do this by running `conda init` in your terminal.

> Don't feel overwhelmed by the terminal. You will get used to it over time. It is much quicker than using a graphical interface.

## Install Python

Finally, you can install Python in your environment using `conda`.

1. Open your terminal.
2. Create a new environment for Python. You can name the environment anything you like. In this example, we name the environment `python-env`.

```shell
conda create --name python-env
```

3. Activate the environment.

```shell
conda activate python-env
```


4. Install Python in the environment.

```shell
conda install python
```

you can specify the version of Python you want to install. For example, to install Python 3.8:

```shell
conda install python=3.11.9
```

5. Check if Python is installed correctly.

```shell
python --version
```

You should see the version of Python you installed.

## Key Takeaways

- **Python Script**: A plain text file with `.py` extension.
- **Python Interpreter**: A program that translates Python scripts into binary code.
- **IDE**, **Code Editor**: Software that helps you write and run Python scripts.
- **Terminal**: A command-line interface where you can run Python scripts and interact with the computer.
- **Environment**: A separate room where you can install different versions of Python and packages.
- **Conda**: A package manager that allows you to create and manage different environments.
- **Miniconda**: A minimal version of `conda` that only includes `conda` and Python.
- **Anaconda**: A full version of `conda` that includes `conda`, Python, and many other packages.
- **Install Python**: Install Python in your environment using `conda`.
- **Check Python**: Check if Python is installed correctly using `python --version`.    

