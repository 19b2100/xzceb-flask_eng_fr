import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_translation(self):
        # Test for translation of 'Hello' to French
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
        # Test for translation of empty string
        self.assertEqual(english_to_french(''), '')
        
        # Test for translation of a non-existent word
        self.assertNotEqual(english_to_french('xyz123'), 'Bonjour')
    
    def test_french_to_english_translation(self):
        # Test for translation of 'Bonjour' to English
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
        # Test for translation of empty string
        self.assertEqual(french_to_english(''), '')
        
        # Test for translation of a non-existent word
        self.assertNotEqual(french_to_english('xyz123'), 'Hello')

if __name__ == '__main__':
    unittest.main()
