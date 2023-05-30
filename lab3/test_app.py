import unittest
import math
import app

class TestApp(unittest.TestCase):

    def test_perform_division(self):
        opm = app.OperationsManager(7, 0)
        result = opm.perform_division()
        self.assertTrue(math.isnan(result))

if __name__ == '__main__':
    unittest.main()
