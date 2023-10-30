import math
from fractions import Fraction


class MyFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ValueError("denominator cannot be 0!!")
        common_divisor = math.gcd(numerator, denominator)

        # Simplify the fraction by dividing both numerator and denominator by the GCD
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        if self.denominator < 0 or self.numerator < 0:
            return f"-{abs(self.numerator) / abs(self.denominator)}"
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return MyFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return MyFraction(new_numerator, new_denominator)


fraction = MyFraction(-3, 6  )
other_fraction = MyFraction(4, 9)

add_result = fraction + other_fraction
mul_result = fraction * other_fraction

print("Original fraction: ", fraction)
print("When a new fraction is added to the fraction, we get: ", add_result)
print("When a new fraction is multiplied by the fraction, we get: ", mul_result)