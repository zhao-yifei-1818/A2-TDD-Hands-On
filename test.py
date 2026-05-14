import unittest
from check_pwd import check_pwd

'''check_pwd accepts a string and returns a boolean: True if it meets the criteria listed below, otherwise it returns False:

Must contain at least one digit
Must contain at least one symbol from: ~`!@#$%^&*()_+-= (copy and paste to avoid missing characters) These are the only symbols that will meet this requirement. Other symbols may be present, but they won't satisfy this requirement.'''
class TestCase(unittest.TestCase):

    def test1(self):
        input = ""
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        input = "Passwor"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test3(self):
        input = "Passwordpassword12345"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test4(self):
        input = "PASSWORDPASSWORD1234"
        expected = False
        self.assertEqual(check_pwd(input), expected)
    
    def test5(self):
        input = "passwordpassword1234"
        expected = False
        self.assertEqual(check_pwd(input), expected)
    
    def test6(self):
        input = "Passwordpassword"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test7(self):
        input = "Passwordpassword1234"
        expected = False
        self.assertEqual(check_pwd(input), expected)

if __name__ == '__main__':
    unittest.main()