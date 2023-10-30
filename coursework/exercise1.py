# Write a pyhton program with functions and import that fomr another file

class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        sum = self.a + self.b
        return sum

    def subtraction(self):
        difference = self.a - self.b
        return difference

    def multiplication(self):
        product = self.a * self.b
        return product

    def division(self):
        quotient = self.a / self.b
        if self.b == 0:
            raise ZeroDivisionError("You cannot divide a number by zero: ")
        else:
            return quotient


numbers = Arithmetic(7, 8)

print(numbers.addition())
print(numbers.division())
print(numbers.subtraction())
print(numbers.multiplication())


        



