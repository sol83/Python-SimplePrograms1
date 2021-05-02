"""
Perimeter of a triangle

Prompt the user to enter the lengths of each side of a triangle
and then calculate and print the perimeter of the triangle
(the sum of all of the side lengths).

Here's a sample run of the program:

$ python perimeter.py
What is the length of side 1? 3
What is the length of side 2? 4
What is the length of side 3? 5.5
The perimeter of the triangle is 1
"""

def main():
    side1 = float(input("What is the lenght of side 1? "))
    side2 = float(input("What is the lenght of side 2? "))
    side3 = float(input("What is the lenght of side 3? "))
    print("The perimeter of the triangle is", (side1 + side2 + side3))
    # Or like this:
    # print("The perimeter of the triangle is" + str(side1 + side2 + side3))

if __name__ == "__main__":
    main()