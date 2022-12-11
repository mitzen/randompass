import unittest
from randompass import RandomPasswordGenerator

class RandomPasswordTest(unittest.TestCase):
    def test_random_password_length(self):
        pwd = RandomPasswordGenerator()
        result = pwd.generate_password()
        print(result)
        self.assertIsNotNone(result)

print(__name__)

if __name__ == '__main__':
    unittest.main()

