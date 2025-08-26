# Write a program that asks for the names of all the classes you are taking this semester
# Save these class names in a list
# Print all the items in your list, one per line

# Introduction and asking the user how many classes they're taking
print("Welcome to the beginning of your semester!")
number_of_classes = int(input("How many classes are you taking this semester? "))

# Created an empty list to store the users class names
classes_list = []

# for loop used to retrieve class name(s) from the user
for i in range(number_of_classes):
    class_name = input(f"Enter the name of the class #{i + 1}: ")
    classes_list.append(class_name)

# Displays the list of classes one per line
print("\nHere are the classes you are taking this semester: ")
for class_name in classes_list:
    print(class_name)