# Human API

`human` is an API for querying human intelligence.


### Installation

```
pip install human
```


## Getting Started


### Connecting
```python
import human

human.username = '...'
human.password = '...'
```

### Asking
```python
from human import regex_utils

q = human.Query.create('How many people live in the US?', regex_utils.INT)
```

### Answering
# Text: How old are you?
# Regex: ^-?\d+$
q = human.Query.get() 

# ValueError
r = human.Response.create('Not sure', q)

# Success!
r = human.Response.create('42', q)
```


