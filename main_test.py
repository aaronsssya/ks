import unittest
import main

class _mainTest(unittest.TestCase):
    def test_message(self):
    	m = 'hello'
    	r = main.message(m)
    	self.assertEqual(m, r)

if __name__ == '__main__':
    unittest.main()