def triangle(a, b, c):
    if a**2 + b**2 == c**2:
        print("It is a right angled triangle.")
    elif a**2 + c**2 == b**2:
        print("It is a right angled triangle.")
    elif b**2 + c**2 == a**2:
        print("It is a right angled triangle.")
    else:
        print("It is not a right angled triangle.")


a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

triangle(a, b, c)