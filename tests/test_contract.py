#tests/test_contract.py

#tests/test_contract.py
import unittest

from contracting.client import ContractingClient
client = ContractingClient()

with open('../relief_app.py') as f:
    code = f.read()
    client.submit(code, name='my_token')

class MyTestCase(unittest.TestCase):
    def test_supply(self):
        my_token = client.get_contract('my_token')
        self.assertEqual(my_token.quick_read('S', 'me'), 100)

if __name__ == '__main__':
    unittest.main()


# tests/test_contract.py
# ...

class MyTestCase(unittest.TestCase):
    def test_supply(self):
        # Get contract reference
        my_token = client.get_contract('my_token')
        # Assert token balance for 'me'
        self.assertEqual(my_token.quick_read('S', 'me'), 100)

    def test_transfer(self):
        # set transaction sender
        client.signer = 'me'
        # Get contract reference
        my_token = client.get_contract('my_token')
        # Call transfer method
        my_token.transfer(
            amount=20,
            receiver='you'
        )
        # Assert token balance for 'me'
        self.assertEqual(my_token.quick_read('S', 'me'), 80)
        # Assert token balance for 'you'
        self.assertEqual(my_token.quick_read('S', 'you'), 20)