#Write a program that asks the user to enter the width and length of a room. Once
#the values have been read, your program should compute and display the area of the
#room. The length and the width will be entered floating point numbers. Include
#units in your prompt and output message; either feet or meters, depending on which
#unit you are more comfortable working with.

#Read the input values from the user

length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))

#Compute area of the room

area = length * width

#Display the result

print("The area of the room is", area, "square feet")
