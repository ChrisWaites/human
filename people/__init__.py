import coreapi
import random
import re

from people import regex_utils


global username
global password
global schema_url

schema_url = 'http://127.0.0.1:8000/schema/'
username = None
password = None


def connect(f):
    def _connect(*args, **kwargs):
        client = coreapi.Client(auth=coreapi.auth.BasicAuthentication(username, password))
        schema = client.get(schema_url)
        return f(client, schema, *args, **kwargs)
    return _connect


def connect_no_auth(f):
    def _connect_no_auth(*args, **kwargs):
        client = coreapi.Client()
        schema = client.get(schema_url)
        return f(client, schema, *args, **kwargs)
    return _connect_no_auth


class User:
    @connect_no_auth
    def create(client, schema, email, username, password):
        return client.action(
            schema,
            ['users', 'create'],
            {'email': email, 'username': username, 'password': password}
        )


class Payment:
    @connect
    def list(client, schema):
        return client.action(
            schema,
            ['payments', 'list'],
            {}
        )

    @connect
    def create(client, schema, token, queries):
        return client.action(
            schema,
            ['payments', 'create'],
            {'token': token, 'queries': [query['id'] for query in queries]}
        )

    @connect
    def read(client, schema, query):
        return client.action(
            schema,
            ['payments', 'read'],
            {'id': query['id']}
        )


class Transfer:
    @connect
    def list(client, schema):
        return client.action(
            schema,
            ['transfers', 'list'],
            {}
        )

    @connect
    def create(client, schema, token, responses):
        return client.action(
            schema,
            ['transfers', 'create'],
            {'token': token, 'responses': [response['id'] for response in responses]}
        )

    @connect
    def read(client, schema, query):
        return client.action(
            schema,
            ['transfers', 'read'],
            {'id': query['id']}
        )


class Query:
    @connect
    def list(client, schema):
        return client.action(
            schema,
            ['queries', 'list'],
            {}
        )

    @connect
    def create(client, schema, text, regex=regex_utils.ANY):
        return client.action(
            schema,
            ['queries', 'create'],
            {'text': text, 'regex': regex}
        )

    @connect
    def read(client, schema, query):
        return client.action(
            schema,
            ['queries', 'read'],
            {'id': query['id']}
        )

    @connect
    def get(client, schema):
        try:
            return client.action(
                schema,
                ['queries', 'get']
            )
        except Exception as e:
            raise Exception('No queries present.')


class Response:
    @connect
    def list(client, schema):
        return client.action(
            schema,
            ['responses', 'list'],
            {}
        )

    @connect
    def create(client, schema, text, query):
        return client.action(
            schema,
            ['responses', 'create'],
            {'text': text, 'query': query['id']}
        )

    @connect
    def read(client, schema, response):
        return client.action(
            schema,
            ['responses', 'read'],
            {'id': response['id']}
        )

