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

### Asking a Query
```python
>>> human.Query.create('How many people live in the US?', human.regex_utils.NONNEG_INT)

OrderedDict([('text', 'How many people live in the US?'), ('regex', '^\\d+$')])
```

### Answering a Query
```
>>> query = human.Query.get() 

OrderedDict([('id', 4), ('text', 'How old are you in years?'), ('regex', '^\\d+$'), ('response', None), ('created', '2018-04-04T20:50:24.560157Z')])

r = human.Response.create('idk', q)

coreapi.exceptions.ErrorMessage: <Error: 400 Bad Request>
    non_field_errors: [
    "Response text 'idk' does not match query regex r'^\\d+$'"
]

r = human.Response.create('42', q)

>>> OrderedDict([('text', '42'), ('query', 4)])
```

## Acknowledgements

Worked on at the [Recurse Center](https://www.recurse.com/) in NYC

