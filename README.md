# pywmit

[![Maintainability](https://api.codeclimate.com/v1/badges/23edcbcbfc0eed7637eb/maintainability)](https://codeclimate.com/github/lrusso96/pywm/maintainability) ![License: GPL v3](https://img.shields.io/badge/License-MIT-blue.svg)

## Examples

```python
from pywmit import check

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

## Dependencies

- [mwklient](https://github.com/lrusso96/mwklient)
