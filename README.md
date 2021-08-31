# Pygoto

Use goto in Python

## Installation

### From PyPI

```sh
pip3 install pygoto
```

### From GitHub

```sh
pip3 install git+https://github.com/donno2048/pygoto
```

## Usage / Examples

```py
from goto import goto
flag = False
flag = not flag
print(0)
if flag:
    goto(3)
print(1)
```

```py
0
0
1
```

```py
from goto import goto
sum = 0
for i in range(10):
    sum += i
    if i == 5:
        goto(7)
print(sum)
```

```py
15
```

```py
from goto import goto
def zero(): 1/0
goto(5)
zero()
print("Done!")
```

```py
Done!
```

```py
from goto import goto
def zero(): 1/0
goto(4)
zero()
print("Done!")
```

```py
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    zero()
  File "main.py", line 2, in zero
    def zero(): 1/0
ZeroDivisionError: division by zero
```

```py
from goto import goto
def zero(): 1/0
goto(3)
zero()
print("Done!")
```

```py
You have passed the recursion limit, please check your goto
```
