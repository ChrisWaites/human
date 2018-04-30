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
    Attributes:
        email (str)
        username (str)
        password (str)
    """

    @connect(False)
    def create(client, schema, email, username, password):
        """
        Args:
            email (str): The new account's email
            username (str): The new account's username
            password (str): The new account's password
        """
        return client.action(
            schema,
            ['users', 'create'],
            {'email': email, 'username': username, 'password': password},
        )


class Deposit:
    """
    Attributes:
        stripeToken (str):
        amount (int):
    """

    @connect()
    def list(client, schema):
        """
        """
        return client.action(
            schema,
            ['deposits', 'list'],
        )

    @connect()
    def read(client, schema, id):
        """
        Args:
            id (str):
        """
        return client.action(
            schema,
            ['deposits', 'read'],
            {'id': id},
        )

    @connect()
    def create(client, schema, stripeToken, amount):
        """
        Args:
            stripeToken (int):
            amount (int):
        """
        return client.action(
            schema,
            ['deposits', 'create'],
            {'stripeToken': stripeToken, 'amount': amount},
        )

        
class Transfer:
    """
    Attributes:
        amount (int):
    """

    @connect()
    def list(client, schema):
        """
        """
        return client.action(
            schema,
            ['transfers', 'list'],
        )

    @connect()
    def read(client, schema, id):
        """
        Args:
            id (str):
        """
        return client.action(
            schema,
            ['transfers', 'read'],
            {'id': id},
        )

    @connect()
    def create(client, schema, amount):
        """
        Args:
            amount (int):
        """
        return client.action(
            schema,
            ['transfers', 'create'],
            {'amount': amount},
        )


class Attribute:
    """
    Attributes:
        key (str):
        value (str):
    """

    @connect()
    def list(client, schema):
        """
        """
        return client.action(
            schema,
            ['attributes', 'list'],
        )

    @connect()
    def read(client, schema, id):
        """
        Args:
            id (str):
        """
        return client.action(
            schema,
            ['attributes', 'read'],
            {'id': id},
        )

    @connect()
    def create(client, schema, key, value):
        """
        Args:
            key (str):
            value (str):
        """
        return client.action(
            schema,
            ['attributes', 'create'],
            {'key': key, 'value': value},
        )

    @connect()
    def destroy(client, schema, id):
        """
        Args:
            id (str):
        """
        return client.action(
            schema,
            ['attributes', 'destroy'],
            {'id': id},
        )


class Query:
    """
    Attributes:
        text (str):
        regex (str):
        callback (str):
    """

    @connect()
    def list(client, schema):
        """
        """
        return client.action(
            schema,
            ['queries', 'list'],
        )

    @connect()
    def create(client, schema, text, regex=regex.ANY):
        """
        Args:
            text (str):
            regex (str):
        """
        return client.action(
            schema,
            ['queries', 'create'],
            {'text': text, 'regex': regex},
        )

    @connect()
    def read(client, schema, id):
        """
        Args:
            id (str):
        """
        return client.action(
            schema,
            ['queries', 'read'],
            {'id': id}
        )

    @connect()
    def get(client, schema):
        """
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
    Attributes:
        text (str):
        query (str):
    """

    @connect()
    def list(client, schema):
        """
        """
        return client.action(
            schema,
            ['responses', 'list'],
        )

    @connect()
    def create(client, schema, text, query_id):
        """
        Args:
            text (str):
            query_id (str):
        """
        return client.action(
            schema,
            ['responses', 'create'],
            {'text': text, 'query': query_id},
        )

    @connect()
    def read(client, schema, id):
        """
        Args:
            id (str):
        """
        return client.action(
            schema,
            ['responses', 'read'],
            {'id': id},
        )


class Rating:
    """
    Attributes:
        satisfactory (bool):
        response (str):
    """

    @connect()
    def list(client, schema):
        """
        """
        return client.action(
            schema,
            ['ratings', 'list'],
        )

    @connect()
    def create(client, schema, satisfactory, response_id):
        """
        Args:
            satisfactory (bool):
            response_id (str):
        """
        return client.action(
            schema,
            ['ratings', 'create'],
            {'satisfactory': satisfactory, 'response': response_id},
        )

    @connect()
    def read(client, schema, id):
        """
        Args:
            id (str):
        """
        return client.action(
            schema,
            ['ratings', 'read'],
            {'id': id},
        )

    @connect()
    def destroy(client, schema, id):
        """
        Args:
            id (str):
        """
        return client.action(
            schema,
            ['attributes', 'destroy'],
            {'id': id},
        )

