# When a user wants anything else besides coffee or tea you inform the user that the required beverage is not available
print("Turning on the machine...")

beverage = input("Do you want tea or coffee? ").lower()

if beverage == "tea":
    print("Preparing tea...")
elif beverage == "coffee":
    print("Preparing Coffee")
else:
    print(f"Sorry, {beverage.capitalize()} is not available")

print("Turning off the machine")