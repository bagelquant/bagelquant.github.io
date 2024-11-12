---
tags:
  - python
---

## Conda

Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.


## Understand environment

An environment is a directory that contains a specific collection of conda packages that you have installed. It could separate different versions of Python, different packages, or even different versions of packages. You can easily activate or deactivate environments, which is how you switch between them.

Imagine computer is a big house, and each environment is a room in the house. When you activate an environment, you "enter" the room. When you install a package, you install it in the room you are currently in. If you switch rooms, you can install a different version of the package in the new room. If you have a package installed in one room, it doesn't affect other rooms.

Why do we need environments? 

- Different projects may require different versions of packages.
- Compatibility issues between packages.
- Easy to share the environment with others.

## Conda command

Using a new environment: 

- Create a new environment: 
    - `conda create --name <ENV_NAME>`
    - `conda create --name <NAME> python==3.13`
- Activate the environment (Enter the room): 
    - `conda activate <ENV_NAME>`
- Install python: 
    - `conda install python`
    - `conda install python==3.13`
- Install a package:
    - `conda install <PACKAGE_NAME>`
    - or `pip install <PACKAGE_NAME>`
- Deactivate the environment (Exit the room): 
    - `conda deactivate`

Manage environments:

- All environments list: 
    - `conda env list`
- All package inside specific environment: 
    - You must activate the environment first.
    - `conda activate <ENV_NAME>`
    - Show current environment packages: `conda list`
- Uninstall an environment: 
    - `conda env remove --name <ENV_NAME>`  
- Export environment:
    - `conda env export > environment.yml`

