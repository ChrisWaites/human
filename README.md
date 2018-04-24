# People API

`people` is an API for requesting human intervention.


### Installation

```
pip install people
```


## Getting Started

```python
>>> import people
```

### Connecting
```python
>>> people.User.create('example@email.com', 'example_username', 'example_password')

>>> people.username = 'example_username'
>>> people.password = 'example_password'
```

### Funding Your Account

Payment info is completely handled by [Stripe](https://stripe.com/), ensuring your payment security.

To deposit funds, login and visit `https://people-api-server.herokuapp.com/checkout/?amount=DESIRED_DEPOSIT_AMOUNT`

You should see your balance afterwards within your profile.


### Creating Queries
```python
>>> people.Query.create(
    "Translate the following sentence to English: Qui n'avance pas, recule."
)

>>> people.Query.create(
    "Is this an image of a [cat], a [dog], or [neither]? https://imgur.com/...",
    people.regex.union('cat', 'dog', 'neither')
)

>>> people.Query.create(
    "How many cars are in this image? https://imgur.com/...",
    people.regex.NONNEG_INT
)

>>> people.Query.create(
    "How positive is this paragraph on a scale from 0.0 to 1.0? https://...",
    people.regex.FLOAT_ZERO_TO_ONE
)

```

### Creating Responses
```python
>>> query = people.Query.get() 

>>> query['text']

"How many cars are in this image? https://imgur.com/...",

>>> query['regex']

r'd+'

>>> response = people.Response.create('Not sure.', query['id'])

coreapi.exceptions.ErrorMessage: <Error: 400 Bad Request>
    non_field_errors: [
    "Response text 'idk' does not match query regex r'd+'"
]

>>> response = people.Response.create('3', query['id'])
```

