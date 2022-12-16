import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : IV Anthony
    Date : November 2022
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : - a numerator int
              - a denominator int greater than zero
        POST : - a object of type Fraction
        RAISES : ZeroDivisionError if the denominator is equal to 0
        """
        if den == 0:
            raise ZeroDivisionError
        pgcd = math.gcd(num, den)
        self.__num = int(num / pgcd)
        self.__den = int(den / pgcd)

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : /
        POST : a string that represents the reduced of the fraction
        """
        if self.__den == 1:
            return "The reduced form of the fraction is " + str(self.__num)
        elif self.__num < 0 and self.__den < 0:
            return "The reduced form of the fraction is " + str(abs(self.__num)) + "/" + str(abs(self.__den))
        elif self.__num > 0 > self.__den:
            return "The reduced form of the fraction is -" + str(self.__num) + "/" + str(abs(self.__den))
        else:
            return "The reduced form of the fraction is " + str(self.__num) + "/" + str(self.__den)

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : /
        POST : a string that represents the reduced of the fraction as a mixed number
        """
        if self.is_zero():
            return "The reduced form of the fraction as a mixed number is 0"
        else:
            number_float = (self.__num / self.__den)
            whole_number = math.floor(number_float)
            new_num = self.__num - (self.__den * whole_number)
            return "The reduced form of the fraction as a mixed number is " + str(whole_number) + " + " + str(
                abs(new_num)) + "/" + str(abs(self.__den))

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : /
         POST : Receives a new fraction whose value is the sum of self and other
         """
        new_num = self.__num * other.__den + self.__den * other.__num
        new_den = self.__den * other.__den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : /
        POST : Receives a new fraction whose value is the subtraction of self and other
        """
        new_num = self.__num * other.__den - self.__den * other.__num
        new_den = self.__den * other.__den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : /
        POST : Receives a new fraction whose value is the multiplication of self and other
        """
        new_num = self.__num * other.__num
        new_den = self.__den * other.__den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : /
        POST : Receives a new fraction whose value is the division of self and other
        """
        new_num = self.__num * other.__den
        new_den = self.__den * other.__num
        return Fraction(new_num, new_den)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : /
        POST : - If other is different from zero: receives a new fraction whose value is the power of self by other
               - If other = 0 -> returns 1
        """
        if other == 0:
            return 1
        else:
            new_num = self.__num ** other
            new_den = self.__den ** other
            return Fraction(new_num, new_den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : /
        POST : Return True if the 2 fractions passed in parameters are equal, return False otherwise

        """
        return (self.__num == other.__num) and (self.__den == other.__den)

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : /
        POST : Return the decimal value of the fraction
        """
        return self.__num / self.__den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : /
        POST : Return True if the numerator is 0, return False otherwise.
        """
        return self.__num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : /
        POST : Return True if integer, return False otherwise
        """
        return self.__num % self.__den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : /
        POST : Return True if the result of the fraction is between 0 and 1, return False otherwise
        """
        return abs(self.__num) < abs(self.__den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : /
        POST : Return True if the numerator is 1 in its reduced form, return False otherwise
        """
        return self.__num == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : /
        POST : Return True if the fractions are adjacent, return False otherwise
        """
        fraction_diff = self - other
        return abs(fraction_diff.numerator) == 1
