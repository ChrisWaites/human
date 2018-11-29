# [People API](https://people.launchaco.com) 👨‍💻

People is an API for requesting on-demand human input.

For more details, check out our [documentation](https://people.readthedocs.io)!

```python
from people import Query, Response
 
Query.create(
  'How many cars are in this image? http://...',
  regex.nonneg_int,
  'http://callback.url/'
)

# POST http://callback.url/
# {
#   'response': '2',
#   'query': {
#     ...
#   }
# }
 
query = Query.get()
print(query.text)
 
>>> 'Is this person smiling? Respond [yes] or [no]. http://...'
 
Response.create('yes', query)
```

### Installation

```
pip install people
```

### Authentication

```python
import people
from people import User

# Registration API
User.create('example@email.com', 'example_username', 'example_password')

# Set auth details
people.username = 'example_username'
people.password = 'example_password'
```

### Funding

#### Paying for queries

Transactions are handled using [Stripe](https://stripe.com/) to ensure your security.

First, [login and register](https://people-api-server.herokuapp.com/register) for a Stripe account connected to our platform. You should see your Stripe account id update within your [profile](https://people-api-server.herokuapp.com/profile).

Then you'll need to deposit funds. Log in and visit `https://people-api-server.herokuapp.com/deposit/?amount=AMOUNT`, replacing `AMOUNT` with the amount you intend to deposit in cents. You should see your balance afterwards within your [profile](https://people-api-server.herokuapp.com/profile).

#### Getting paid to answer queries

To get paid for answering queries, simply submit responses! Then, to redeem your balance, create a `Transfer` instance as so.

```python
from people import Transfer

transfer = Transfer.create(AMOUNT) 
```

