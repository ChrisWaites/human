# [People API](https://people.launchaco.com/)

People is an API for requesting human interaction.

Official documentation located [here](https://people.readthedocs.io).


### Installation

```
pip install people
```


### Getting Started

```python
>>> import people

>>> people.User.create('example@email.com', 'example_username', 'example_password')

>>> people.username = 'example_username'
>>> people.password = 'example_password'
```

### Account Funds

Transactions are entirely handled using [Stripe](https://stripe.com/), ensuring your security. First, login and [register](https://people-api-server.herokuapp.com/register) for a Stripe account connected to our platform. You should see your Stripe account id update within your [profile](https://people-api-server.herokuapp.com/profile).

To deposit funds, login and visit `https://people-api-server.herokuapp.com/deposit/?amount=AMOUNT`, replacing `AMOUNT` with the amount you intend to deposit in cents. You should see your balance afterwards within your [profile](https://people-api-server.herokuapp.com/profile).

To redeem your balance, simply create a `Transfer` instance as so.

```python
>>> transfer = people.Transfer.create(AMOUNT) 
```


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
```

### Reading Responses
```python
>>> query = people.Query.list()[0]
>>> query['response']['text']
```

### Creating Responses
```python
>>> query = people.Query.get() 
>>> query['text']

"How many cars are in this image? http://...",

>>> response = people.Response.create('Not sure.', query['id'])

coreapi.exceptions.ErrorMessage: <Error: 400 Bad Request>
    non_field_errors: [
    "Response text 'Not sure.' does not match query regex r'd+'"
]

>>> response = people.Response.create('3', query['id'])
```


### Providing Feedback

You should always provide feedback to a subset of responses to minimize likelihood of receiving poor responses in the future.

```python
>>> people.Rating.create(True, good_response['id'])
>>> people.Rating.create(False, bad_response['id'])
```

