import unittest
import math
import app

from unittest.mock import patch

class TestApp(unittest.TestCase):

    def test_perform_division(self):
        opm = app.OperationsManager(7, 0)
        result = opm.perform_division()
        self.assertTrue(math.isnan(result))

    @patch('builtins.input', return_value='3.4')
    def test_float_input(self, input):
        try:
            app.login_success()
        except:
            self.fail()

    @patch('builtins.input', return_value='a')
    def test_char_input(self, input):
        self.assertRaises(ValueError, app.login_success)

if __name__ == '__main__':
    unittest.main()
