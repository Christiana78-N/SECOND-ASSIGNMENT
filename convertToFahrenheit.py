# Ask the user for the city name.
city_input = input("Enter the name of a city: ")

# Ask the user for the current temperature in Fahrenheit.
Fahrenheit_input = input("Enter current temperature in Fahrenheit: ")

# Convert the temperature to float
Fahrenheit = float(Fahrenheit_input)

# Convert the temperature to Celsuis
convert_to_Celsuis = (Fahrenheit - 32) * 5/9

# Check if the temperature is below freezing point.
if convert_to_Celsuis < 0 :
    print("Alert: The temperature is below freezing point.")
else:
    print("The temperature is above the freezing point")

# Print the user input in a formatted string
# Always print the temperature in Celsuis(up to one decimal point).
print(f"The current temperature in {city_input} is {convert_to_Celsuis:.1f} degrees Celsius")