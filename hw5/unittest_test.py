__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import unittest

def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return b


class Test_Fibonnaci(unittest.TestCase):

    def setUp(self):
        # выполняется в начале теста автоматически
        pass

    def test_math(self):
        self.assertEqual(fib(0), 1)

    def test_bad_data(self):
        self.assertEqual(fib('котики'), -1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
