# Ask the user to enter an integer using input
number_input = input("Enter an integer: ")

# Convert the input to an integer
number = int(number_input)

#  Check if it's between 10 and 50 or 0.
if (number >= 10 and number <= 50) or number == 0:
    print("Inclusive")