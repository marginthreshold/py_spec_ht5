def check_triangle(side1: int, side2: int, side3: int):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        print("The triangle can't be existed")
    elif side1 == side2 == side3:
        print("This triangle is equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("This triangle is isosceles")
    else:
        print("This triangle is scalene")


side_1 = int(input("Enter the first side of new triangle:"))
side_2 = int(input("Enter the second side of new triangle:"))
side_3 = int(input("Enter the third side of new triangle:"))

check_triangle(side_1, side_2, side_3)
