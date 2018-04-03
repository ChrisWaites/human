# Human API

`human` is an API for querying human intelligence.


### Installation

```
pip install human
```


## Getting Started


### Connecting
```python
from human import Human

h = Human(username='...', password='...')
```

### Asking
```python
q = h.ask('What is the meaning of life?')
...
q.responses()
>>> ['Love', 'Happiness', 'Memes', '42']
```

### Responding
```python
q = h.get()
>>> Question(text='What is 2+2?', regex='^-?\d+$')
q.respond('Idk')
>>> ValueError("'Idk' does not match regex '^-?\d+$'")
q.respond('4')
```

