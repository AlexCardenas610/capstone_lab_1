# Write a program that asks for you name and the month you were born
# Your program should print
# A greeting to you, using your name
# A message with the number of letters in your name
# A 'Happy birthday month!' message if you were born in the current month
# Easier - compare the user's input to "January" or "August" or whatever the current month is
# Harder - use Python to figure out the current month and use that in the comparison.

# Asks the user to enter their name and the month they were born in
users_name = input('Hello! Please enter your name: ')
birthday_month = input('Enter the month you were born in: ')

# Prints the userds entered name
print(f'Hello {users_name}')

# Using length to figure out how many letters are int he users name
letters_in_name = len(users_name)

# Prints the number of letters in the users name using length
print(f'You have {letters_in_name} letters in your name.')

# If the user enters 'august' (the current month) as their birthday month then it prints a happy birthday month message
# Otherwise, no birthday month message appears
if birthday_month.lower() == 'august':
    print('Happy Birthday month!')