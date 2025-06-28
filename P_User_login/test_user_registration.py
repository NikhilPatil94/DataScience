import unittest
from user_registration import validate_name, validate_email, validate_password, register_user

class TestUserValidation(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(validate_name("Nikhil"))

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            validate_name("x")

    def test_valid_email(self):
        self.assertTrue(validate_email("test@example.com"))

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            validate_email("bademail")

    def test_valid_password(self):
        self.assertTrue(validate_password("Secure123"))

    def test_invalid_password_length(self):
        with self.assertRaises(ValueError):
            validate_password("S1x")

    def test_invalid_password_no_caps(self):
        with self.assertRaises(ValueError):
            validate_password("secure123")

    def test_invalid_password_no_digit(self):
        with self.assertRaises(ValueError):
            validate_password("SecureOnly")

    def test_register_user_success(self):
        user = register_user("Meera", "meera@mail.com", "Test1234")
        self.assertEqual(user["name"], "Meera")
        self.assertEqual(user["email"], "meera@mail.com")
        self.assertEqual(user["password"], "########")  # 8 characters masked

    def test_register_user_fail(self):
        result = register_user("x", "bademail", "weak")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
