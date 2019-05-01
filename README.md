# Attribute Router

![Travis (.org)](https://img.shields.io/travis/FKLC/AttributeRouter.svg?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/AttributeRouter.svg?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/AttributeRouter.svg?style=flat-square)
![GitHub release](https://img.shields.io/github/release/FKLC/AttributeRouter.svg?style=flat-square)
![GitHub](https://img.shields.io/github/license/FKLC/AttributeRouter.svg?style=flat-square)

Attribute Router is a library that chains calls of attributes of class and if regex matches it returns method.

## Quick Start

```python
import re

from attribute_router import Router


class Printer(Router):
    def __init__(self):
        super().__init__(
            routes={
                re.compile(" (.*) PRINT"): self.print_match
            },
            join_char=" "
        )

    def print_match(self, prefix, _match):
        print(prefix, _match.group(1))

Printer().hello.world('!').again.PRINT("Hello and")
```

So to define routes we use compiled regex and the method itself also don't forget to inherit from `attribute_router.Router`

---

## Installation

Library is on PyPi so just run

```
pip install AttributeRouter
```
