import unittest

import euler


class IsPrimeTestCase(unittest.TestCase):
    def test_isprime(self):
        self.assertEqual(euler.isprime(1), False)
        self.assertEqual(euler.isprime(2), True)
        self.assertEqual(euler.isprime(3), True)
        self.assertEqual(euler.isprime(4), False)
        self.assertEqual(euler.isprime(5), True)


if __name__ == '__main__':
    unittest.main()
