import unittest
from translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertRaises(ValueError, english_to_french, None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class testFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertRaises(ValueError, french_to_english, None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()