# Human API

`people` is an API for querying human intelligence.


### Installation

```
pip install people
```


## Getting Started


### Connecting
```python
>>> import people

>>> people.username = '...'
>>> people.password = '...'
```

### Asking a Query
```python
>>> people.Query.create('How many people live in the US?', people.regex_utils.NONNEG_INT)

OrderedDict([('text', 'How many people live in the US?'), ('regex', '^\\d+$')])
```

### Answering a Query
```python
>>> query = people.Query.get() 

OrderedDict([('id', 4), ('text', 'How old are you in years?'), ('regex', '^\\d+$'), ('response', None), ('created', '2018-04-04T20:50:24.560157Z')])

>>> response = people.Response.create('idk', query)

coreapi.exceptions.ErrorMessage: <Error: 400 Bad Request>
    non_field_errors: [
    "Response text 'idk' does not match query regex r'^\\d+$'"
]

>>> response = people.Response.create('42', query)

OrderedDict([('text', '42'), ('query', 4)])
```

