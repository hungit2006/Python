# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

##
# Compute the total weight of the order
#

# The weighS of each widget and gizmo
EACH_WIDGET_WEIGH = 75
EACH_GIZMO_WEIGH = 112

# Read input from the user
numbers_of_widget = int(input("The number of widgets from the user: "))
numbers_of_gizmo = int(input("The number of gizmo from the user: "))

# Compute the sum
total = numbers_of_widget * EACH_WIDGET_WEIGH + numbers_of_gizmo * EACH_GIZMO_WEIGH

# Display the result
print("The total weight of the order: ", total,"grams")
