import coreapi
import regex_util
import re
import random


SCHEMA_URL = 'http://127.0.0.1:8000/schema/'


class Human:
    def __init__(self, username, password, schema_url=SCHEMA_URL):
        self.client = coreapi.Client(
            auth=coreapi.auth.BasicAuthentication(
                username=username,
                password=password
            )
        )
        self.schema = self.client.get(schema_url)

    def ask(self, text, regex=regex_util.ANY):
        return self.client.action(
            self.schema,
            ['queries', 'create'],
            {'text': text, 'regex': regex}
        )

    def get(self):
        queries = self.client.action(
            self.schema,
            ['queries', 'list']
        )
        return random.choice(queries)

    def respond(self, text, query):
        if re.fullmatch(query['regex'], text):
            self.client.action(
                self.schema,
                ['responses', 'create'],
                {'text': text, 'query': query['id']}
            )
        else:
            raise ValueError('\'{}\' does not match regex \'{}\''.format(text, query['regex']))


