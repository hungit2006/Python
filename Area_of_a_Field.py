# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

# Computer the area of a field, reporting the result in acres

SQFT_PER_ACRE = 43560

# Read input from the user

length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feed: "))

# Compute the area in acres

acres = length * width / SQFT_PER_ACRE

# Display the result

print("The area of the field is:", acres, "acres")