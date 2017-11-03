from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Humberto Nagato', cpf='12345678901',
                    email='humberto.nagatog@gmail.com', phone='27-99930-7451')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):

        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):

        expect = ['contato@eventex.com.br', 'humberto.nagatog@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Humberto Nagato',
            '12345678901',
            'humberto.nagatog@gmail.com',
            '27-99930-7451',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

