import unittest
from check_pwd import check_pwd


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

    def test8(self):
        input = "Passwordpassword123!"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test9(self):
        input = "1234Abc!"
        expected = True
        self.assertEqual(check_pwd(input), expected)


if __name__ == "__main__":
    unittest.main()
