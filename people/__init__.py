import coreapi
from people import regex


global username
global password
global schema_url

schema_url = 'https://people-api-server.herokuapp.com/schema'


def connect(authenticate=True):
    def decorator(f):
        def _connect(*args, **kwargs):
            auth = coreapi.auth.BasicAuthentication(username, password) if authenticate else None 
            client = coreapi.Client(auth=auth)
            schema = client.get(schema_url)
            return f(client, schema, *args, **kwargs)
        return _connect
    return decorator


class User:
    @connect(False)
    def create(client, schema, email, username, password):
        return client.action(
            schema,
            ['users', 'create'],
            {'email': email, 'username': username, 'password': password}
        )


class Profile:
    @connect()
    def list(client, schema):
        return client.action(
            schema,
            ['profiles', 'list'],
            {}
        )

    @connect()
    def read(client, schema, profile):
        return client.action(
            schema,
            ['profiles', 'read'],
            {'id': profile['id']}
        )

    @connect()
    def update(client, schema, customer_id):
        return client.action(
            schema,
            ['profiles', 'update'],
            {'customer_id': customer_id}
        )


class Transaction:
    @connect()
    def list(client, schema):
        return client.action(
            schema,
            ['transactions', 'list'],
            {}
        )

    @connect()
    def read(client, schema, transaction):
        return client.action(
            schema,
            ['transactions', 'read'],
            {'id': transaction['id']}
        )

    @connect()
    def create(client, schema, amount):
        return client.action(
            schema,
            ['transactions', 'create'],
            {'amount': amount}
        )


class Attribute:
    @connect()
    def list(client, schema):
        return client.action(
            schema,
            ['attributes', 'list'],
            {}
        )

    @connect()
    def read(client, schema, attribute):
        return client.action(
            schema,
            ['attributes', 'read'],
            {'id': attribute['id']}
        )

    @connect()
    def create(client, schema, key, value):
        return client.action(
            schema,
            ['attributes', 'create'],
            {'key': key, 'value': value}
        )

    @connect()
    def destroy(client, schema, attribute):
        return client.action(
            schema,
            ['attributes', 'destroy'],
            {'id': attribute['id']}
        )


class Query:
    @connect()
    def list(client, schema):
        return client.action(
            schema,
            ['queries', 'list'],
            {}
        )

    @connect()
    def create(client, schema, text, regex=regex_utils.ANY):
        return client.action(
            schema,
            ['queries', 'create'],
            {'text': text, 'regex': regex}
        )

    @connect()
    def read(client, schema, query):
        return client.action(
            schema,
            ['queries', 'read'],
            {'id': query['id']}
        )

    @connect()
    def get(client, schema):
        try:
            return client.action(
                schema,
                ['queries', 'get']
            )
        except Exception as e:
            raise Exception('No queries present.')


class Response:
    @connect()
    def list(client, schema):
        return client.action(
            schema,
            ['responses', 'list'],
            {}
        )

    @connect()
    def create(client, schema, text, query):
        return client.action(
            schema,
            ['responses', 'create'],
            {'text': text, 'query': query['id']}
        )

    @connect()
    def read(client, schema, response):
        return client.action(
            schema,
            ['responses', 'read'],
            {'id': response['id']}
        )

