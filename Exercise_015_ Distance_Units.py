# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

##
# Calculate distance in inches, yards and miles
#
IN_PER_INCH = 12
IN_PER_YARD = 0.333333
IN_PER_MILE = 0.00018939

# Read input from the user
feet = float(input("Enter a measurement in feet: "))

# Compute the equivalent number of inches, yards, miles
inches = feet * IN_PER_INCH
yards = feet * IN_PER_YARD
miles = feet * IN_PER_MILE

#Display the result
print("Your measurement in inches: ", inches, "inches")
print("Your measurement in yards: ", yards, "yards")
print("Your measurement in miles: ", miles, "miles")

