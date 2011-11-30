import unittest

import euler


class IsPalindromeTestCase(unittest.TestCase):
    def test_ispalindrome(self):
        self.assertEqual(euler.ispalindrome(1), True)
        self.assertEqual(euler.ispalindrome(11), True)
        self.assertEqual(euler.ispalindrome(12), False)
        self.assertEqual(euler.ispalindrome(111), True)
        self.assertEqual(euler.ispalindrome(123), False)
        self.assertEqual(euler.ispalindrome(1221), True)
        self.assertEqual(euler.ispalindrome(1231), False)


class IsPandigital(unittest.TestCase):
    def test_ispandigital(self):
        self.assertEqual(euler.ispandigital(1), True)
        self.assertEqual(euler.ispandigital(2), False)
        self.assertEqual(euler.ispandigital(2143), True)
        self.assertEqual(euler.ispandigital(2145), False)


class IsPrimeTestCase(unittest.TestCase):
    def test_isprime(self):
        self.assertEqual(euler.isprime(1), False)
        self.assertEqual(euler.isprime(2), True)
        self.assertEqual(euler.isprime(3), True)
        self.assertEqual(euler.isprime(4), False)
        self.assertEqual(euler.isprime(5), True)


if __name__ == '__main__':
    unittest.main()
