import unittest
from check_pwd import check_pwd

'''check_pwd accepts a string and returns a boolean: True if it meets the criteria listed below, otherwise it returns False:

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
        input = "Passwordpasswordpass"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test4(self):
        input = "Passwordpasswordpassw"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test5(self):
        input = "PASSWORD"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test6(self):
        input = "Password"
        expected = True
        self.assertEqual(check_pwd(input), expected)
    
if __name__ == '__main__':
    unittest.main()