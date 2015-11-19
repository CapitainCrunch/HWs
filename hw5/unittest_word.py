__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import unittest


def drink(word):
    arr = ['выпью', 'выпьешь', 'выпьет', 'выпьем', 'выпейте', 'выпьют', 'выпил', 'выпила', 'выпило', 'выпили',
    'выпивший', 'выпив', 'выпивши', 'выпитый']
    if word in arr:
        return True
    return False

class TestWord(unittest.TestCase):

    def setUp(self):
        # выполняется в начале теста автоматически
        pass

    def test_future(self):
        arr = ['выпью', 'выпьешь', 'выпьет', 'выпьем',
               'выпейте', 'выпьют']
        for i in arr:
            self.assertEqual(drink(i), True)

    def test_past(self):
        arr = ['выпил', 'выпила', 'выпило', 'выпили']
        for i in arr:
            self.assertEqual(drink(i), True)

    def test_another_forms(self):
        arr = ['выпивший', 'выпив', 'выпивши', 'выпитый']
        for i in arr:
            self.assertEqual(drink(i), True)

    def test_bad_data(self):
        arr = ['выпиваю', 'выпиваешь']
        for i in arr:
            self.assertEqual(drink(i), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)
