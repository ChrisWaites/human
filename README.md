# [People API (In Development)](https://people.launchaco.com/)

People is an API for requesting human interaction.

```python
>>> import people

>>> query = people.Query.create(
    "How many people are in this image? http://...",
    people.regex.nonneg_int,
    "https://callback.url/"
)

>>> people.Query.read(query)['response']['text']

4
```

Official documentation located [here](https://people.readthedocs.io).


### Installation

```
pip install people
```

### Connecting

```python
>>> people.User.create('example@email.com', 'example_username', 'example_password')

>>> people.username = 'example_username'
>>> people.password = 'example_password'
```

### Funding

Transactions are entirely handled using [Stripe](https://stripe.com/), ensuring your security.

First, login and [register](https://people-api-server.herokuapp.com/register) for a Stripe account connected to our platform. You should see your Stripe account id update within your [profile](https://people-api-server.herokuapp.com/profile).

If you intend to submit queries, you must deposit funds. Login and visit `https://people-api-server.herokuapp.com/deposit/?amount=AMOUNT`, replacing `AMOUNT` with the amount you intend to deposit in cents. You should see your balance afterwards within your [profile](https://people-api-server.herokuapp.com/profile).

If you intend to answer queries, to redeem your balance, create a `Transfer` instance as so.

```python
>>> transfer = people.Transfer.create(AMOUNT) 
```

