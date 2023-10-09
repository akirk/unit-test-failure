import unittest
import strings

class TestStrings(unittest.TestCase):
    def test_concatenate_strings(self):
        self.assertEqual(strings.concatenate_strings('Hello', ' World'), 'Hello World')

    def test_whitespace_stripping(self):
        self.assertEqual(strings.concatenate_strings('Hello', ' World '), 'Hello World')  # Failing test

if __name__ == '__main__':
    unittest.main()
