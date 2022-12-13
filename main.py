from fraction import Fraction

if __name__ == "__main__":
    a = Fraction(8, 4)
    b = Fraction(3, 2)

    print("fonction : __str__")
    print(a)
    print(b)

    print("\nfonction : as_mixed_number()")
    print(b.as_mixed_number())

    print("\nfonction : __add__")
    print(a.__add__(b))

    print("\nfonction : __sub__")
    print(a.__sub__(b))

    print("\nfonction : __mul__")
    print(a.__mul__(b))

    print("\nfonction : __truediv__")
    print(a.__truediv__(b))

    print("\nfonction : __power__")
    print(a.__pow__(2))

    print("\nfonction : __eq__")
    print(a.__eq__(b))

    print("\nfonction : __float__")
    print(a.__float__())

    print("\nfonction : is_zero")
    print(a.is_zero())

    print("\nfonction : is_integer")
    print(a.is_integer())

    print("\nfonction : is_proper")
    print(a.is_proper())

    print("\nfonction : is_unit")
    print(a.is_unit())

    print("\nfonction : is_adjacent_to")
    print(a.is_adjacent_to(b))





