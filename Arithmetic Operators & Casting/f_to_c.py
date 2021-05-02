"""
Fahrenheit to Celsius

Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!)
and outputs the temperature converted to Celsius.

The equation you should use for converting from Fahrenheit to Celsius is the following:

degrees_celsius = (degrees_fahrenheit - 32) * 5/9

Here's a sample run of the program:

$ python f_to_c.py
Enter temperature in Fahrenheit: 76
Temperature: 76.0F = 24.444444444444443C
"""

def main():
    temp_f = float(input("Enter temperature in farenheit: "))
    temp_c = (temp_f - 32) * 5/9
    print("Temperature: " + str(temp_f) + "F = " + str(temp_c) + "C")

if __name__ == "__main__":
    main()