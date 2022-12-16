import unittest

from fraction import Fraction


class test_fraction(unittest.TestCase):
    def test_init(self):
        fraction1 = Fraction(5, 8)
        self.assertEqual(fraction1.numerator, 5)
        self.assertEqual(fraction1.denominator, 8)
        fraction2 = Fraction(-5, -8)
        self.assertEqual(fraction2.numerator, -5)
        self.assertEqual(fraction2.denominator, -8)
        fraction3 = Fraction(-5, 8)
        self.assertEqual(fraction3.numerator, -5)
        self.assertEqual(fraction3.denominator, 8)
        fraction4 = Fraction(5, -8)
        self.assertEqual(fraction4.numerator, 5)
        self.assertEqual(fraction4.denominator, -8)
        fraction5 = Fraction(0, 8)
        self.assertEqual(fraction5.numerator, 0)
        self.assertEqual(fraction5.denominator, 1)
        self.assertRaises(ZeroDivisionError, Fraction, 5, 0)
        self.assertRaises(ZeroDivisionError, Fraction, 0, 0)

    def test_str(self):
        self.assertEqual(Fraction(15, 7).__str__(), "The reduced form of the fraction is 15/7")
        self.assertEqual(Fraction(-15, -7).__str__(), "The reduced form of the fraction is 15/7")
        self.assertEqual(Fraction(-15, 7).__str__(), "The reduced form of the fraction is -15/7")
        self.assertEqual(Fraction(15, -7).__str__(), "The reduced form of the fraction is -15/7")
        self.assertEqual(Fraction(0, 7).__str__(), "The reduced form of the fraction is 0")
        with self.assertRaises(ZeroDivisionError):
            Fraction(15, 0).__str__()
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0).__str__()

    def test_as_mixed_number(self):
        self.assertEqual(Fraction(5, 2).as_mixed_number(), "The reduced form of the fraction as a mixed number is 2 + "
                                                           "1/2")
        self.assertEqual(Fraction(-5, -2).as_mixed_number(), "The reduced form of the fraction as a mixed number is 2 "
                                                             "+ 1/2")
        self.assertEqual(Fraction(-5, 2).as_mixed_number(), "The reduced form of the fraction as a mixed number is -3 "
                                                            "+ 1/2")
        self.assertEqual(Fraction(5, -2).as_mixed_number(), "The reduced form of the fraction as a mixed number is -3 "
                                                            "+ 1/2")
        self.assertEqual(Fraction(0, 2).as_mixed_number(), "The reduced form of the fraction as a mixed number is 0")
        with self.assertRaises(ZeroDivisionError):
            Fraction(5, 0).as_mixed_number()
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0).as_mixed_number()

    def test_add(self):
        calcul1 = Fraction(3, 5) + Fraction(4, 7)
        self.assertEqual(str(calcul1), "The reduced form of the fraction is 41/35")
        calcul2 = Fraction(-3, -5) + Fraction(-4, -7)
        self.assertEqual(str(calcul2), "The reduced form of the fraction is 41/35")
        calcul3 = Fraction(-3, 5) + Fraction(-4, 7)
        self.assertEqual(str(calcul3), "The reduced form of the fraction is -41/35")
        calcul4 = Fraction(3, -5) + Fraction(4, -7)
        self.assertEqual(str(calcul4), "The reduced form of the fraction is -41/35")
        calcul5 = Fraction(0, 5) + Fraction(0, 7)
        self.assertEqual(str(calcul5), "The reduced form of the fraction is 0")
        with self.assertRaises(ZeroDivisionError):
            Fraction(3, 0) + Fraction(4, 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0) + Fraction(0, 0)

    def test_sub(self):
        calcul1 = Fraction(10, 4) - Fraction(5, 6)
        self.assertEqual(str(calcul1), "The reduced form of the fraction is 5/3")
        calcul2 = Fraction(-10, -4) - Fraction(-5, -6)
        self.assertEqual(str(calcul2), "The reduced form of the fraction is 5/3")
        calcul3 = Fraction(-10, 4) - Fraction(-5, 6)
        self.assertEqual(str(calcul3), "The reduced form of the fraction is -5/3")
        calcul4 = Fraction(10, -4) - Fraction(5, -6)
        self.assertEqual(str(calcul4), "The reduced form of the fraction is -5/3")
        calcul4 = Fraction(0, 4) - Fraction(0, 6)
        self.assertEqual(str(calcul4), "The reduced form of the fraction is 0")
        with self.assertRaises(ZeroDivisionError):
            Fraction(10, 0) - Fraction(5, 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0) - Fraction(0, 0)

    def test_mul(self):
        calcul1 = Fraction(6, 3) * Fraction(2, 5)
        self.assertEqual(str(calcul1), "The reduced form of the fraction is 4/5")
        calcul2 = Fraction(-6, -3) * Fraction(-2, -5)
        self.assertEqual(str(calcul2), "The reduced form of the fraction is 4/5")
        calcul3 = Fraction(-6, 3) * Fraction(-2, 5)
        self.assertEqual(str(calcul3), "The reduced form of the fraction is 4/5")
        calcul4 = Fraction(6, -3) * Fraction(2, -5)
        self.assertEqual(str(calcul4), "The reduced form of the fraction is 4/5")
        calcul5 = Fraction(0, 3) * Fraction(0, 5)
        self.assertEqual(str(calcul5), "The reduced form of the fraction is 0")
        with self.assertRaises(ZeroDivisionError):
            Fraction(6, 0) * Fraction(2, 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0) * Fraction(0, 0)

    def test_truediv(self):
        calcul1 = Fraction(2, 3) / Fraction(5, 7)
        self.assertEqual(str(calcul1), "The reduced form of the fraction is 14/15")
        calcul2 = Fraction(-2, -3) / Fraction(-5, -7)
        self.assertEqual(str(calcul2), "The reduced form of the fraction is 14/15")
        calcul3 = Fraction(-2, 3) / Fraction(-5, 7)
        self.assertEqual(str(calcul3), "The reduced form of the fraction is 14/15")
        calcul4 = Fraction(2, -3) / Fraction(5, -7)
        self.assertEqual(str(calcul4), "The reduced form of the fraction is 14/15")
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 3) / Fraction(0, 7)
        with self.assertRaises(ZeroDivisionError):
            Fraction(2, 0) / Fraction(5, 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0) / Fraction(0, 0)

    def test_pow(self):
        calcul1 = Fraction(4, 5) ** 2
        self.assertEqual(str(calcul1), "The reduced form of the fraction is 16/25")
        calcul2 = Fraction(-4, -5) ** 2
        self.assertEqual(str(calcul2), "The reduced form of the fraction is 16/25")
        calcul3 = Fraction(-4, 5) ** 2
        self.assertEqual(str(calcul3), "The reduced form of the fraction is 16/25")
        calcul4 = Fraction(4, -5) ** 2
        self.assertEqual(str(calcul4), "The reduced form of the fraction is 16/25")
        calcul5 = Fraction(0, 5) ** 2
        self.assertEqual(str(calcul5), "The reduced form of the fraction is 0")
        calcul5 = Fraction(4, 5) ** 0
        self.assertEqual(str(calcul5), "1")
        with self.assertRaises(ZeroDivisionError):
            Fraction(4, 0) ** 2
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0) ** 0

    def test_eq(self):
        calcul1 = Fraction(4, 5) == Fraction(8, 10)
        self.assertTrue(calcul1)
        calcul2 = Fraction(-4, -5) == Fraction(-8, -10)
        self.assertTrue(calcul2)
        calcul3 = Fraction(-4, 5) == Fraction(8, -10)
        self.assertTrue(calcul3)
        calcul4 = Fraction(4, -5) == Fraction(-8, 10)
        self.assertTrue(calcul4)
        calcul5 = Fraction(0, 5) == Fraction(0, 10)
        self.assertTrue(calcul5)
        calcul6 = Fraction(7, 5) == Fraction(1, 10)
        self.assertFalse(calcul6)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0).__eq__(Fraction(5, 0))
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0).__eq__(Fraction(0, 0))

    def test_float(self):
        self.assertEqual(Fraction(1, 4).__float__(), 0.25)
        self.assertEqual(Fraction(-1, -4).__float__(), 0.25)
        self.assertEqual(Fraction(-1, 4).__float__(), -0.25)
        self.assertEqual(Fraction(1, -4).__float__(), -0.25)
        self.assertEqual(Fraction(0, 4).__float__(), 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0).__float__()
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0).__float__()

    def test_is_zero(self):
        self.assertFalse(Fraction(2, 6).is_zero())
        self.assertFalse(Fraction(-2, -6).is_zero())
        self.assertFalse(Fraction(-2, 6).is_zero())
        self.assertFalse(Fraction(2, -6).is_zero())
        self.assertTrue(Fraction(0, 6).is_zero())
        with self.assertRaises(ZeroDivisionError):
            Fraction(2, 0).is_zero()
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0).is_zero()

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertTrue(Fraction(-4, -2).is_integer())
        self.assertTrue(Fraction(-4, 2).is_integer())
        self.assertTrue(Fraction(4, -2).is_integer())
        self.assertFalse(Fraction(3, 2).is_integer())
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0).is_integer()
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0).is_integer()

    def test_is_proper(self):
        self.assertTrue(Fraction(4, 7).is_proper())
        self.assertTrue(Fraction(-4, -7).is_proper())
        self.assertTrue(Fraction(-4, 7).is_proper())
        self.assertTrue(Fraction(4, -7).is_proper())
        self.assertFalse(Fraction(4, 2).is_proper())
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0).is_proper()
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0).is_proper()

    def test_is_unit(self):
        self.assertTrue(Fraction(5, 5).is_unit())
        self.assertFalse(Fraction(-3, 5).is_unit())
        self.assertFalse(Fraction(4, 2).is_unit())
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0).is_unit()
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0).is_unit()

    def test_adjacent_to(self):
        self.assertTrue(Fraction(1, 4).is_adjacent_to(Fraction(1, 6)))
        self.assertTrue(Fraction(-1, -4).is_adjacent_to(Fraction(-1, -6)))
        self.assertTrue(Fraction(-1, 4).is_adjacent_to(Fraction(-1, 6)))
        self.assertTrue(Fraction(1, -4).is_adjacent_to(Fraction(-1, 6)))
        self.assertFalse(Fraction(0, 4).is_adjacent_to(Fraction(0, 6)))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0).is_adjacent_to(Fraction(1, 0))
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0).is_adjacent_to(Fraction(0, 0))






