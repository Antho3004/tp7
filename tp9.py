import unittest

from fraction import Fraction


class test_fraction(unittest.TestCase):
    def test_init(self):
        fraction1 = Fraction(5, 3)
        self.assertEqual(fraction1.numerator, 5)
        self.assertEqual(fraction1.denominator, 3)
        fraction2 = Fraction(-8, 6)
        self.assertEqual(fraction2.numerator, -4)
        self.assertEqual(fraction2.denominator, 3)

    def test_str(self):
        self.assertEqual(Fraction(5, 2).__str__(), "The reduced form of the fraction is 5/2")
        self.assertEqual(Fraction(10, 5).__str__(), "The reduced form of the fraction is 2")
        self.assertEqual(Fraction(-5, 2).__str__(), "The reduced form of the fraction is -5/2")

    def test_as_mixed_number(self):
        self.assertEqual(Fraction(5, 4).as_mixed_number(), "The reduced form of the fraction as a mixed number is 1 + 1/4")

    def test_add(self):
        calcul1 = Fraction(4, 2) + Fraction(7, 2)
        self.assertEqual(str(calcul1), "The reduced form of the fraction is 11/2")
        calcul2 = Fraction(10, 2) + Fraction(8, 4)
        self.assertEqual(str(calcul2), "The reduced form of the fraction is 7")
        calcul3 = Fraction(-3, 2) + Fraction(-5, 2)
        self.assertEqual(str(calcul3), "The reduced form of the fraction is -4")
        calcul4 = Fraction(5, 5) + Fraction(-9, 5)
        self.assertEqual(str(calcul4), "The reduced form of the fraction is -4/5")
        #calcul5 = Fraction(-3, 2) + Fraction(5, -2)
        #self.assertEqual(str(calcul5), "The reduced form of the fraction is -4")

    def test_sub(self):
        calcul1 = Fraction(6, 3) - Fraction(2, 3)
        self.assertEqual(str(calcul1), "The reduced form of the fraction is 4/3")
        calcul2 = Fraction(2, 3) - Fraction(6, 3)
        self.assertEqual(str(calcul2), "The reduced form of the fraction is -4/3")
        calcul3 = Fraction(-6, 3) - Fraction(-2, 3)
        self.assertEqual(str(calcul3), "The reduced form of the fraction is -4/3")
        calcul4 = Fraction(6, 3) - Fraction(-2, -3)
        self.assertEqual(str(calcul4), "The reduced form of the fraction is 4/3")

    def test_mul(self):
        calcul1 = Fraction(6, 3) * Fraction(2, 5)
        self.assertEqual(str(calcul1), "The reduced form of the fraction is 4/5")
        calcul2 = Fraction(6, 3) * Fraction(5, 4)
        self.assertEqual(str(calcul2), "The reduced form of the fraction is 5/2")
        calcul3 = Fraction(7, 3) * Fraction(4, 5)
        self.assertEqual(str(calcul3), "The reduced form of the fraction is 28/15")
        calcul5 = Fraction(-8, 3) * Fraction(2, 3)
        self.assertEqual(str(calcul5), "The reduced form of the fraction is -16/9")