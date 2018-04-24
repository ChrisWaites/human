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


### Creating a Query
```python
>>> query = people.Query.create('How many people live in the US?', people.regex_utils.NONNEG_INT)

>>> query['text']

'How many people live in the US?'

>>> query['regex']

r'd+'
```

### Creating a Response
```python
>>> query = people.Query.get() 

>>> query['text']

'How many people live in the US?'

>>> response = people.Response.create('idk', query['id'])

coreapi.exceptions.ErrorMessage: <Error: 400 Bad Request>
    non_field_errors: [
    "Response text 'idk' does not match query regex r'd+'"
]

>>> response = people.Response.create('42', query['id'])
```

