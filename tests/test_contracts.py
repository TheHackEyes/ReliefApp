#tests/test_contract.py

#tests/test_contract.py
import unittest

from contracting.client import ContractingClient
client = ContractingClient()
#with open('../relief_app.py') as f:
with open('../relief_app.py') as f:
    code = f.read()
    client.submit(code, name='my_token')

class MyTestCase(unittest.TestCase):
    def test_supply(self):
        my_token = client.get_contract('my_token')
        self.assertEqual(my_token.quick_read('S', 'me'), 100)

if __name__ == '__main__':
    unittest.main()