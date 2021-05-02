"""
Square number

Ask the user for a number and print its square
(the product of the number times itself).

Here's a sample run of the program:

$ python square.py
Type a number to see its square: 4
4.0 squared is 16.0
"""

def main():
    num = float(input("Type a number to see its square: "))
    print(num, "squared is", num**2)
    # The follwing is also possible:
    # print(str(num) + " squared is " + str(num**2))

if __name__ == "__main__":
    main()