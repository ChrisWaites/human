"""
People is an API for requesting human intervention.
"""

import coreapi
from functools import wraps
from people import regex


global username
global password
global schema_url

schema_url = 'https://people-api-server.herokuapp.com/schema'


def connect(authenticate=True):
    def decorator(f):
        @wraps(f)
        def _connect(*args, **kwargs):
            auth = coreapi.auth.BasicAuthentication(username, password) if authenticate else None 
            client = coreapi.Client(auth=auth)
            schema = client.get(schema_url)
            return f(client, schema, *args, **kwargs)
        return _connect
    return decorator


class User:
    """
    """

    @connect(False)
    def create(client, schema, email, username, password):
        """
        Creates a new User instance. 
        
        Args:
            email (str): The new account's email.
            username (str): The new account's username.
            password (str): The new account's password.
        """
        return client.action(
            schema,
            ['users', 'create'],
            {'email': email, 'username': username, 'password': password},
        )


class Deposit:
    """
    """

    @connect()
    def list(client, schema):
        """
        Retrieves all Deposit instances associated with the current user.
        """
        return client.action(
            schema,
            ['deposits', 'list'],
        )

    @connect()
    def read(client, schema, id):
        """
        Retrieves the details of a given Deposit instance.

        Args:
            id (str): The id of the deposit.
        """
        return client.action(
            schema,
            ['deposits', 'read'],
            {'id': id},
        )

    @connect()
    def create(client, schema, stripeToken, amount):
        """
        Creates a new Deposit instance. 

        Args:
            stripeToken (int): A Stripe token representing a valid card.
            amount (int): The amount of the deposit in cents.
        """
        return client.action(
            schema,
            ['deposits', 'create'],
            {'stripeToken': stripeToken, 'amount': amount},
        )

        
class Transfer:
    """
    """

    @connect()
    def list(client, schema):
        """
        Retrieves all Transfer instances associated with the current user.
        """
        return client.action(
            schema,
            ['transfers', 'list'],
        )

    @connect()
    def read(client, schema, id):
        """
        Retrieves the details of a given Transfer instance.

        Args:
            id (str): The id of the transfer.
        """
        return client.action(
            schema,
            ['transfers', 'read'],
            {'id': id},
        )

    @connect()
    def create(client, schema, amount):
        """
        Creates a new Transfer instance.

        Args:
            amount (int): The amount of the transfer in cents.
        """
        return client.action(
            schema,
            ['transfers', 'create'],
            {'amount': amount},
        )


class Attribute:
    """
    A key-value relationship representing a profile attribute.
    E.g. 'education': 'university of california, berkeley'
    """

    @connect()
    def list(client, schema):
        """
        Retrieves all Attribute instances associated with the current user.
        """
        return client.action(
            schema,
            ['attributes', 'list'],
        )

    @connect()
    def read(client, schema, id):
        """
        Retrieves the details of a given Attribute instance.

        Args:
            id (str): The id of the attribute.
        """
        return client.action(
            schema,
            ['attributes', 'read'],
            {'id': id},
        )

    @connect()
    def create(client, schema, key, value):
        """
        Creates a new Transfer instance.
        
        Args:
            key (str): The attribute tag.
            value (str): The attribute value.
        """
        return client.action(
            schema,
            ['attributes', 'create'],
            {'key': key, 'value': value},
        )

    @connect()
    def destroy(client, schema, id):
        """
        Deletes a given Attribute instance.

        Args:
            id (str): The id of the attribute.
        """
        return client.action(
            schema,
            ['attributes', 'destroy'],
            {'id': id},
        )


class Query:
    """
    """

    @connect()
    def list(client, schema):
        """
        Retrieves all Query instances associated with the current user.
        """
        return client.action(
            schema,
            ['queries', 'list'],
        )

    @connect()
    def create(client, schema, text, regex=regex.ANY):
        """
        Creates a new Query instance. 

        Args:
            text (str): The text to be included in the query.
            regex (str): A regex the response must match to be valid.
        """
        return client.action(
            schema,
            ['queries', 'create'],
            {'text': text, 'regex': regex},
        )

    @connect()
    def read(client, schema, id):
        """
        Retrieves the details of a given Query instance.

        Args:
            id (str): The id of the query.
        """
        return client.action(
            schema,
            ['queries', 'read'],
            {'id': id}
        )

    @connect()
    def get(client, schema):
        """
        Requests an unanswered Query compatible with the current user.
        """
        try:
            return client.action(
                schema,
                ['queries', 'get'],
            )
        except Exception as e:
            raise Exception('No queries present.')


class Response:
    """
    """

    @connect()
    def list(client, schema):
        """
        Retrieves all Response instances associated with the current user.
        """
        return client.action(
            schema,
            ['responses', 'list'],
        )

    @connect()
    def create(client, schema, text, query_id):
        """
        Creates a new Response instance.

        Args:
            text (str): The text for the response.
            query_id (str): The id of the target query.
        """
        return client.action(
            schema,
            ['responses', 'create'],
            {'text': text, 'query': query_id},
        )

    @connect()
    def read(client, schema, id):
        """
        Retrieves the details of a given Response instance.

        Args:
            id (str): The id of the response.
        """
        return client.action(
            schema,
            ['responses', 'read'],
            {'id': id},
        )


class Rating:
    """
    """

    @connect()
    def list(client, schema):
        """
        Retrieves all Rating instances associated with the current user.
        """
        return client.action(
            schema,
            ['ratings', 'list'],
        )

    @connect()
    def create(client, schema, satisfactory, response_id):
        """
        Creates a new Rating instance.

        Args:
            satisfactory (bool): True if the response is satisfactory, False otherwise.
            response_id (str): The id of the response.
        """
        return client.action(
            schema,
            ['ratings', 'create'],
            {'satisfactory': satisfactory, 'response': response_id},
        )

    @connect()
    def read(client, schema, id):
        """
        Retrieves the details of a given Rating instance.

        Args:
            id (str): The id of the rating.
        """
        return client.action(
            schema,
            ['ratings', 'read'],
            {'id': id},
        )

    @connect()
    def destroy(client, schema, id):
        """
        Deletes a given Rating instance.

        Args:
            id (str): The id of the rating.
        """
        return client.action(
            schema,
            ['attributes', 'destroy'],
            {'id': id},
        )

