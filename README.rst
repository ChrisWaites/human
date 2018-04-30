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

Charges are handled using [Checkout](https://stripe.com/checkout) by [Stripe](https://stripe.com/), ensuring your security by handling all secure information client side.

To deposit funds, login and visit `https://people-api-server.herokuapp.com/deposit/?amount=AMOUNT`, replacing `AMOUNT` with the amount you intend to deposit in cents.

You should see your balance afterwards within your profile at `https://people-api-server.herokuapp.com/profile`.

If you think there's a discrepency, feel free to email `support@peopleapi.com` with your inquiry.


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
```python
>>> unanswered_query = ... 
>>> response = people.Query.read(unanswered_query['id'])['response']

None

>>> answered_query = ...
>>> response = people.Query.read(answered_query['id'])['response']
>>> response['text']

34.1231
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

### Redeeming from Your Account

To redeem funds, if you haven't already, login and visit `https://people-api-server.herokuapp.com/register` to register for a Stripe account connected to our platform.

You should see your Stripe account id update within your profile at `https://people-api-server.herokuapp.com/profile`.

Now, simply create a Transfer for the amount you intend to redeem in cents.

```python
>>> transfer = people.Transfer.create(50) 
```

### Providing Feedback

Users should feel incentivized to provide feedback on a subset of their responses to minimize their likelihood of receiving future interaction
with poor quality responders.

```python
>>> good_response = ...
>>> people.Rating.create(True, good_response['id'])

>>> bad_response = ...
>>> people.Rating.create(False, bad_response['id'])
```

