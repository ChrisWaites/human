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

Transactions and payment info are completely handled by [Stripe](https://stripe.com/), ensuring your security.

To deposit funds, login and visit `https://people-api-server.herokuapp.com/checkout/?amount=AMOUNT`, replacing `AMOUNT` with the amount you intend to deposit in cents.

You should see your balance afterwards within your profile at `https://people-api-server.herokuapp.com/profile`.

If you want to claim a discrepency, feel free to email `support@peopleapi.com` with your inquiry.


### Creating Queries
```python
>>> people.Query.create(
    "Translate the following sentence to English: Qui n'avance pas, recule."
)

>>> people.Query.create(
    "How many cars are in this image? http://...",
    people.regex.NONNEG_INT
)

>>> people.Query.create(
    "Is this an image of a [cat], a [dog], or [neither]? http://...",
    people.regex.union('cat', 'dog', 'neither')
)

>>> people.Query.create(
    "How positive is this article on a scale from 1 to 5? http://...",
    r'[1-5]'
)
```

### Reading Responses

>>> query = people.Query.create(
    "How many cars are in this image? http://...",
    people.regex.NONNEG_INT
)

>>> try:
>>>     people.Query.read(query['id'])['response']
>>> except Exception as e:
>>>     print('No response.')

No response.

...

>>> try:
>>>     people.Query.read(query['id'])['response']
>>> except Exception as e:
>>>     print('No response.')

5
```

### Creating Responses
```python
>>> query = people.Query.get() 

>>> query['text']

"How many cars are in this image? http://...",

>>> query['regex']

r'd+'

>>> response = people.Response.create('Not sure.', query['id'])

coreapi.exceptions.ErrorMessage: <Error: 400 Bad Request>
    non_field_errors: [
    "Response text 'Not sure.' does not match query regex r'd+'"
]

>>> response = people.Response.create('3', query['id'])
```

### Providing Feedback
```python
>>> good_response = ...

>>> people.Rating.create(True, good_response['id'])

>>> bad_response = ...

>>> people.Rating.create(False, bad_response['id'])
```

