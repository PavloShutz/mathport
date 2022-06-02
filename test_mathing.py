import unittest
import mathing


class TestMathing(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(mathing.calc('2+2'), 4)
        self.assertEqual(mathing.calc('3-7'), -4)
        self.assertEqual(mathing.calc('1+1/0'),
                         "Division by zero!")

    def test_calc_raises_error(self):
        with self.assertRaises(ValueError):
            mathing.calc('r+2')
            mathing.calc('y-9')
            mathing.calc('y/0')


if __name__ == '__main__':
    unittest.main()
