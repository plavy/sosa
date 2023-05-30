import unittest
import math
import io

import app

from unittest import TestCase
from unittest.mock import patch

class TestApp(TestCase):

    def test_perform_division(self):
        opm = app.OperationsManager(7, 0)
        result = opm.perform_division()
        self.assertTrue(math.isnan(result))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='3.4')
    def test_float_input(self, input, output): # pylint: disable=redefined-builtin,unused-argument
        try:
            app.login_success()
            self.assertEqual(output.getvalue(), "1.0\nResult:  3.4\n")
        except: # pylint: disable=bare-except
            self.fail()

    @patch('builtins.input', return_value='a')
    def test_char_input(self, input): # pylint: disable=redefined-builtin,unused-argument
        self.assertRaises(ValueError, app.login_success)

if __name__ == '__main__':
    unittest.main()
