# Write a function that takes the lengths of the two shorter sides of a right triangle as
# its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
# theorem, as the function’s result. Include a main program that reads the lengths of
# the shorter sides of a right triangle from the user, uses your function to compute the
# length of the hypotenuse, and displays the result.
short_side=int(input("Enter a value for the short side: "))
long_side=int(input("Enter a value for the long side: "))
def sides():
    return (long_side**2 + short_side ** 2)**.5
sides()
print ("The Hypotenuse is",sides())
