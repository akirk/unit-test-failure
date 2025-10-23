import unittest
import strings

class TestStrings(unittest.TestCase):
    def test_concatenate_strings(self):
        self.assertEqual(strings.concatenate_strings('Hello', ' World'), 'Hello World')

    def test_concatenate_strings2(self):
        self.assertEqual(strings.concatenate_strings('Hello', ' there'), 'Hello there')

if __name__ == '__main__':
    unittest.main()
