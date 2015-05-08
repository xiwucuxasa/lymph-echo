from lymph.testing import RPCServiceTestCase

from echo import Echo


class EchoTest(RPCServiceTestCase):

    service_class = Echo
    service_name = 'echo'

    def test_echo(self):
        self.assertEqual(
            self.client.echo(text='ciao!'),
            'ciao!'
        )
