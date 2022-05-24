import unittest
import countvowels

class TestAdd(unittest.TestCase):
	def test_count(self):
		self.assertEqual(countvowels.countvowel("hello my name is GLEN"),6)

if __name__ == 'main':
	unittest.main()