---
title: "Fixing mysqlclient Installation Error on macOS (pip + Homebrew)"
tags: 
    - mysql
    - database
    - python
---

Recently I tried to install the mysqlclient Python package using pip, but ran into a frustrating build error. Since this is a common issue for macOS developers, I’m recording the problem and solution here for future reference.

⸻
## The Problem

Running:

```bash
pip install mysqlclient
```

resulted in the following error:

```plaintext
note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.
```

Looking a bit further up in the logs, I noticed:

```bash
/bin/sh: pkg-config: command not found
Trying pkg-config --exists mysqlclient
Command 'pkg-config --exists mysqlclient' returned non-zero exit status 127.

This was the real culprit — the pkg-config tool was missing.
```


## Why pkg-config Matters

mysqlclient is a Python wrapper around the native MySQL client library. To build it from source, the compiler needs to know:

- where to find the MySQL header files
- which libraries to link against

The tool that provides this information is pkg-config. If it isn’t installed, the build fails because pip can’t locate MySQL’s development files.


## The Solution

The fix is straightforward on macOS using Homebrew:

```bash
brew install pkg-config
```

If you don’t already have the MySQL client libraries, you should also install them:

```bash
brew install mysql-client
```

After that, retry the installation:

```bash
pip install mysqlclient
```

This time, the build completed successfully.

