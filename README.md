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

## Usage

```py
from goto import goto
flag = False
flag = not flag
print(0)
if flag:
    goto(3)
print(1)
```

```sh
0
0
1
```
