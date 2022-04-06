import unittest
from form import email_regex, validate

class EmailTest(unittest.TestCase):
    def test_bad(self):
        self.assertFalse(email_regex.match("bad@."))

    def test_good(self):
        self.assertTrue(email_regex.match("test@example.com"))
    
    def test_validation(self):
        cases = [
            ("Hello. How are you?", "test@example.com"),
            ("Your website is so bad", "hater@example.com"),
        ]

        for (q, e) in cases:
            self.assertIsNone(validate(q, e))


if __name__ == "__main__":
    unittest.main()
