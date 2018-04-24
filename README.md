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
    "Translate the following to English: Qui n'avance pas, recule."
)

>>> people.Query.create(
    "How many cars are in this image? https://imgur.com/...",
    people.regex.NONNEG_INT
)

>>> people.Query.create(
    "Is this an image of a [cat] or a [dog]? https://imgur.com/...",
    people.regex.UNION('cat', 'dog')
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

