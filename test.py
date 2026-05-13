import unittest
from check_pwd import check_pwd

'''check_pwd accepts a string and returns a boolean: True if it meets the criteria listed below, otherwise it returns False:

Must be between 8 and 20 characters (inclusive of both bounds)
Must contain at least one lowercase letter (standard English alphabet)
Must contain at least one uppercase letter (standard English alphabet)
Must contain at least one digit
Must contain at least one symbol from: ~`!@#$%^&*()_+-= (copy and paste to avoid missing characters) These are the only symbols that will meet this requirement. Other symbols may be present, but they won't satisfy this requirement.'''
class TestCase(unittest.TestCase):

    def test1(self):
        input = "Passwor"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        input = "Password"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test3(self):
        input = "Passwordpasswordpas"
        expected = True
        self.assertEqual(check_pwd(input), expected)
    
if __name__ == '__main__':
    unittest.main()