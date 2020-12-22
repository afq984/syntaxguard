# syntaxguard

*Use syntax unavailable to unsupported Python versions to show a error message about Python version*

The following won't show the python version hint when run with Python 2.7,
because the code doesn't even parse, the check never runs:

```python
import sys
import getpass

if sys.version_info < (3, 6):
    print('Please use Python 3.6 or later')
    sys.exit(1)


print(f'Hello, {getpass.getuser()}')
```

But this does:

```python
f'Please use Python 3.6 or later'
import getpass

print(f'Hello, {getpass.getuser()}')
```

Example output:

```console
$ python2 hello.py
  File "hello.py", line 1
    f'Please use Python 3.6 or later'
                                    ^
SyntaxError: invalid syntax
```
