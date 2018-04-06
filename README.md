# Human API

`human` is an API for querying human intelligence.


### Installation

```
pip install human
```


## Getting Started


### Connecting
```python
>>> import human

>>> human.username = '...'
>>> human.password = '...'
```

### Asking a Query
```python
>>> human.Query.create('How many people live in the US?', human.regex_utils.NONNEG_INT)

OrderedDict([('text', 'How many people live in the US?'), ('regex', '^\\d+$')])
```

### Answering a Query
```python
>>> query = human.Query.get() 

OrderedDict([('id', 4), ('text', 'How old are you in years?'), ('regex', '^\\d+$'), ('response', None), ('created', '2018-04-04T20:50:24.560157Z')])

>>> response = human.Response.create('idk', query)

coreapi.exceptions.ErrorMessage: <Error: 400 Bad Request>
    non_field_errors: [
    "Response text 'idk' does not match query regex r'^\\d+$'"
]

>>> response = human.Response.create('42', query)

OrderedDict([('text', '42'), ('query', 4)])
```

