import coreapi
import random
import re

from human import regex_utils


global username
global password
global schema_url

schema_url = 'http://127.0.0.1:8000/schema/'
username = 'cw'
password = 'smokeycat'

client = coreapi.Client(auth=coreapi.auth.BasicAuthentication(username, password))
schema = client.get(schema_url)
print(schema)


def connect(f):
    def _connect(*args, **kwargs):
        client = coreapi.Client(auth=coreapi.auth.BasicAuthentication(username, password))
        schema = client.get(schema_url)
        return f(client, schema, *args, **kwargs)
    return _connect


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
    def delete(client, schema, query):
        return client.action(
            schema,
            ['queries', 'delete'],
            {'id': query['id']}
        )

    @connect
    def get(client, schema):
        return client.action(
            schema,
            ['queries', 'get']
        )


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

    @connect
    def delete(client, schema, response):
        return client.action(
            schema,
            ['responses', 'delete'],
            {'id': response['id']}
        )


