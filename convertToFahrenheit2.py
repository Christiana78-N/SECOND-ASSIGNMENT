# Ask the user for city names.
city_input = input("Enter the name of the first city: ")
city_input2 = input("Enter the name of the second city: ")

# Ask the user for the current temperature in Fahrenheit.
Fahrenheit_input = input(f"Please enter current temperature for {city_input} in Fahrenheit: ")
Fahrenheit_input2 = input(f"Please enter current temperature for {city_input2} in Fahrenheit: ")

# Convert the temperature to float
Fahrenheit = float(Fahrenheit_input)
Fahrenheit2 = float(Fahrenheit_input2)

# Convert the temperature to Celsius
convert_to_Celsius = (Fahrenheit - 32) * 5/9
convert_to_Celsius2 = (Fahrenheit2 - 32) * 5/9

# Check if the temperature is below freezing point (0°C).
if convert_to_Celsius < 0 and convert_to_Celsius2 < 0:
    print("Alert: The temperature in both cities is below freezing point.")
elif convert_to_Celsius < 0 or convert_to_Celsius2 < 0:
    print("The temperature in one of the cities is below freezing point.")
else:
    print("The temperature in both cities is above freezing point.")

# Print the user input in a formatted string
# Always print the temperature in Celsius (up to one decimal point).
print(f"The current temperature in {city_input} is {convert_to_Celsius:.1f} degrees Celsius.")
print(f"The current temperature in {city_input2} is {convert_to_Celsius2:.1f} degrees Celsius.")
