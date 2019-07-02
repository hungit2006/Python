# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration

##
# Compute and display the total number of seconds represented by this duration
#
SERCONDS_PER_DAY = 86400
SERCONDS_PER_HOUR = 3600
SERCONDS_PER_MINUTE = 60

#Read input from the user
day = int(input("Enter number of day: "))
hour = int(input("Enter number hours: "))
minute = int(input("Enter number of minute: "))

#Display the result
print("The total number of seconds represented by this duration: ", day * SERCONDS_PER_DAY + hour * SERCONDS_PER_HOUR + minute * SERCONDS_PER_MINUTE, "seconds")


