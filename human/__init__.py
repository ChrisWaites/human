import coreapi
import random
import re

from human import regex_utils


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


class Query:
    @connect
    def list(client, schema):
        return client.action(
            schema,
            ['queries', 'list']
        )

    @connect
    def create(client, schema, text, regex=regex_utils.ANY):
        return client.action(
            schema,
            fields=['queries', 'create'],
            params={'text': text, 'regex': regex}
        )

    @connect
    def get(client, schemea):
        return random.choice(client.action(
            schema,
            ['queries', 'list']
        ))


class Response:
    @connect
    def create(client, schema, text, query):
        if re.fullmatch(query['regex'], text):
            return client.action(
                schema,
                ['responses', 'create'],
                {'text': text, 'query': query['id']}
            )
        else:
            raise ValueError('\'{}\' does not match regex \'{}\''.format(text, query['regex']))


class Attribute:
    @connect
    def list(client, schema):
        return client.action(
            schema,
            ['attributes', 'list']
        )

    @connect
    def create(client, schema, key, value):
        return client.action(
            schema,
            ['attributes', 'create'],
            {'key': key, 'value': value}
        )

