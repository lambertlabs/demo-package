## How To Use
* clone the repo
* activate a virtual environment, perhaps in another project/repository
* run `pip install -e /path/to/locally/cloned/repo`
* create `demo.py`:

```python
from demo_package import utils

print(utils.add_two_numbers(1, 2))
print(utils.get_url('https://www.google.com').status_code)

```

The output should be 

```
3
200
```