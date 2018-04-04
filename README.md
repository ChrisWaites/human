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
q = human.Query.create('How many people live in the US?', human.regex_utils.INT)
>>> OrderedDict([('text', 'How many people live in the US?'), ('regex', '^-?\d+$')])
```

### Answering
```
q = human.Query.get() 
>>> OrderedDict([('id', '0'), ('text', 'What is the meaning of life?'), ('regex', '^-?\d+$')])

r = human.Response.create('Not sure', q)
>>> ValueError("'Not sure' does not match regex '^-?\d+$'")

r = human.Response.create('42', q)
>>> OrderedDict([('id', '0'), ('text', '42'), ('query', '0')])
```

## Acknowledgements

Worked on at the [Recurse Center](https://www.recurse.com/) in NYC

