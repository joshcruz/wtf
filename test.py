from app import app

import unittest

class BasicTestCase(unittest.TestCase):
    def test_hello(self):
        tester = app.test_client()
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()