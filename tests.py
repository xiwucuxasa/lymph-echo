from lymph.testing import RPCServiceTestCase


class EchoTest(RPCServiceTestCase):

    def test_echo(self):
        self.assertEqual(
            self.client.request('echo', {'text': 'ciao!'}),
            'ciao!'
        )
