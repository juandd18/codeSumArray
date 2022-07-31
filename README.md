## Setup

It is recommended to use a python virtual environment such as conda or virtualenv, here we  show the steps with virtualenv but there is no difference.
for more information about virtualenv (http://timsherratt.org/digital-heritage-handbook/docs/python-pip-virtualenv/)

First we are going to activate the virtual environment (if you have any doubts, look at the link shown above)
MacOx or 

Linux
```bash
source YOUR-VIRTUAL-ENV/bin/activate
```

Windows 
```bash
Scripts\activate
```

inside project folder we can run:

```bash
pip install -r requirements.txt 
```

the above command install all libraries needed for main.py

## How to run

to run the code we just need to pass two parameters:

- --sum-value: the target value
- --list: a list of values separeted by space ex: 1 2 3 4 5 6

Example:

```bash
python main.py --sum-value -5 --list 1 -2 -3 7 10
```

## How to run pytest

you just need to run the below command 

```bash
python -m pytest -v
```

