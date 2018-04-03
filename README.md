# Human API

`human` is an API for querying human intelligence.


### Installation

```
pip install humanapi
```


## Getting Started


### Establishing a connection
```
from human import Human
from human import regex_utils

h = Human(username='...', password='...')
```

### Asking a question
```
q = h.ask('What is the meaning of life?')
...
q.responses()
>>> ['Love', 'Happiness', 'Memes', '42']
```

### Responding to a question
```
q = h.get()
>>> Question(text='What is 2+2?', regex='^-?\d+$')
q.respond('Idk')
>>> ValueError("'Idk' does not match regex '^-?\d+$'")
q.respond('4')
```

