"""
Remainder division

Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second
and also the remainder of the division.

Here's a sample run of the program:

$ python remainder.py
Please enter an integer to be divided: 5
Please enter an integer to divide by: 3
The result of this division is 1 with a remainder of 2
"""

def main():
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divide by: "))
    print("The result of this division is", num1//num2, "with a remainder of", num1%num2)

"""
Another solution, more vebose:

def main():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))
    quotient = dividend // divisor
    remainder = dividend % divisor
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))
"""

if __name__ == "__main__":
    main()