## Preface
- This is my first package for me to study how to deploy a python 3 package

## Overview
- This is a repo of Library in Python called `LogMaintainer`
- The package requires Python 3.11.8+

## Installation
```
pip install git+https://github.com/tomche1234/LogMaintainer.git
```

## How to use
```
from LogMaintainer import Log as U


def this_fails():
    x = 1 / 0
    
def main():
   funcName = main.__name__
   try:
      U.running(funcName)
      U.log(funcName, "start run this_fails function")
      this_fails()
   except Exception as e:
      U.exception(funcName, e)

main()
```
### Result
```
2024-11-29 23:58:59.105631:main is running
2024-11-29 23:58:59.105631 main: start run this_fails function
2024-11-29 23:58:59.105631[<class 'ZeroDivisionError'> error happened on main]:division by zero
```