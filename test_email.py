import unittest
from form import email_regex

class EmailTest(unittest.TestCase):
    def test_bad(self):
        self.assertFalse(email_regex.match("bad@."))

    def test_good(self):
        self.assertTrue(email_regex.match("test@example.com"))


if __name__ == "__main__":
    unittest.main()
