# Ask the user to enter their age using input
age_input = input("Enter your age: ")

# Convert the input to an integer
age = int(age_input)

if age < 0:
    print("Age cannot be negative.")
else:
    # Determine the ticket based on age
    if age <= 3:
        print("Free")
    elif age <= 12:
        print("$10")
    elif age <= 64:
        print("$15")
    else:
        print("$5")