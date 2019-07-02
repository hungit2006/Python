# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds
# respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary.

##
# Convert a number of seconds to day, hours, minutes and seconds
#
SERCONDS_PER_DAY = 86400
SERCONDS_PER_HOUR = 3600
SERCONDS_PER_MINUTE = 60

# Read input from the user
seconds = int(input("Enter a number of seconds: "))

# Compute the days, hours, minutes and seconds
days = seconds / SERCONDS_PER_DAY
seconds = seconds % SERCONDS_PER_DAY

hours = seconds / SERCONDS_PER_HOUR
seconds = seconds % SERCONDS_PER_HOUR

minutes = seconds / SERCONDS_PER_MINUTE
seconds = seconds % SERCONDS_PER_MINUTE

# Display the result with the desired formatting
print("The equivalent duration is: ", \
      "%d:%02d:%02d:%02d." % (days, hours,minutes,seconds))
