# Ask the user to enter a numeric grade (0 to 100) using input().
grade_input = input("Please enter a numeric grade (0 to 100): ")

# Convert the input to an integer
grade = int(grade_input)

# Classify  the grade
if grade < 0 or grade > 100:
    print("Please enter a grade between 0 and 100.")
else:
    # Classify the grade as follows:
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    elif grade < 60:
        print("F")
        