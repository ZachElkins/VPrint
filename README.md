# VPrint

![Tests](https://github.com/ZachElkins/VPrint/actions/workflows/tests.yml/badge.svg)

Verbose printing utility for python.

Check it out on [pypi.org](https://pypi.org/project/verbose-print/0.0.1/)!
### Installation and usage

`pip install verbose-print==0.0.1`
```python3
import verbose_print.vprint as vp

def main():
    v = True
    e = "!"
    vp.vprint("Hello", "World", verbose=v, end=e)

if __name__ == "__main__":
    main()
```
