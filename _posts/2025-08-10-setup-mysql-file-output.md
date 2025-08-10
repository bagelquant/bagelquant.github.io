---
title: "Setup MySQL secure_file_priv for File Output"
tags: 
    - mysql
    - database
---

secure_file_priv in MySQL is a server variable that restricts where LOAD DATA INFILE and SELECT ... INTO OUTFILE can read/write files.
You can’t change it directly with SET unless it’s in your MySQL config or startup options — it’s a read-only variable after the server starts.

## Check current setting

In MySQL:

SHOW VARIABLES LIKE 'secure_file_priv';

- If it returns a path, MySQL will only allow file import/export in that directory.
- If it returns an empty string (''), file import/export is allowed from any path.
- If it returns NULL, file import/export is disabled.

## Change the setting

You need to edit MySQL’s configuration file and restart the server.

On macOS (Homebrew install)

Edit:

```bash
vim /opt/homebrew/etc/my.cnf
```

or, if using MariaDB via Homebrew:

```bash
vim /opt/homebrew/etc/my.cnf.d/server.cnf
```

Add under [mysqld]:

secure_file_priv = /absolute/path/to/allowed/dir

Example:

[mysqld]
secure_file_priv = /Users/eric/mysql_secure
vim /opt/homebrew/etc/my.cnf.d/server.cnf

Add under [mysqld]:

secure_file_priv = /absolute/path/to/allowed/dir

Example:

[mysqld]

secure_file_priv = /Users/eric/mysql_secure

Make sure the folder exists and MySQL has permission:

mkdir -p /Users/eric/mysql_secure
chmod 755 /Users/eric/mysql_secure

Restart MySQL:

```bash
brew services restart mysql
# or
brew services restart mariadb
```

## Using without restriction (for dev)

To allow reading/writing from any directory:

[mysqld]
secure_file_priv = ""

Not recommended for production — this removes the restriction entirely.

## Verify after restart

SHOW VARIABLES LIKE 'secure_file_priv';

It should now match the path you set (or be empty if unrestricted).

If you want, I can give you the exact my.cnf edits for your Homebrew MySQL ARM64 install so it works with Python’s LOAD DATA INFILE calls.
Do you want me to prepare that?
