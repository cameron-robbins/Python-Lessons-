# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will
# turn 100 years old. Note: for this exercise, the expectation is that you explicitly
# write out the year (and therefore be out of date the next year). 


name = input("What is your name?")

age = int(input("How old are you?"))


current_year = 2023
birth_year = current_year - age 
year_you_turn_100 = 100 + birth_year


print(f'Hi {name} you will turn 100 in the year {year_you_turn_100}')
