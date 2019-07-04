# Create a program that reads two integers, a and b, from the user.Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab
# Hint: You will probably find the log10 function in the math module helpful
# for computing the second last item in the list.

##
# Demonstrate Python's mathematical operators and its math module
#
# We must import the log10 function from the math module before we call it.
# Import statements normally appear at the top of the file
from math import log10

# Read input values form the user

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Compute and display the sum, difference, product,
# quotient and remainder
print(a, "+", b, "is", a + b)
print(a, "-", b, "is", a - b)
print(a, "*", b, "is", a * b)
print(a, "/", b, "is", a / b)
print(a, "%", b, "is", a % b)

# Compute the logarithm and the power
print("The base 10 logarithm of", a, "is", log10(a))
print(a, "~", b, "is", a**b)
