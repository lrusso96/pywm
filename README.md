# pywmit

[![Maintainability](https://api.codeclimate.com/v1/badges/23edcbcbfc0eed7637eb/maintainability)](https://codeclimate.com/github/lrusso96/pywm/maintainability) ![License: GPL v3](https://img.shields.io/badge/License-MIT-blue.svg)

## Setup

Before you use the library, you need to create a file named **user-config.py** in your _pywikibot directory_. Then set the content of the environment variable **PYWIKIBOT_DIR**.

## Examples

```python
from pywmit.check import check

page_titles = [...]
for page in page_titles:
    check(page)
```

that outputs something like:

```
WARNING: invalid parameter in template...
WARNING: missing required parameter for template...
...
```

## Useful resources

- [Setup Pywikibot user-config.py](https://www.mediawiki.org/wiki/Manual:Pywikibot/user-config.py)
