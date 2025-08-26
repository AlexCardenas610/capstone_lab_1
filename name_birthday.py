# Write a program that asks for you name and the month you were born
# Your program should print
# A greeting to you, using your name
# A message with the number of letters in your name
# A 'Happy birthday month!' message if you were born in the current month

# Harder - use Python to figure out the current and month
# and use that to compare it to your birthday month

users_name = input('Hello! Please enter your name: ')
birthday_month = input('Enter the month you were born in: ')

print(f'Hello {users_name}')

letters_in_name = len(users_name)

print(f'You have {letters_in_name} letters in your name.')

if birthday_month.lower() == 'august':
    print('Happy Birthday month!')