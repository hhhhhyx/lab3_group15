number = int(input("""1) Square
2) Triangle
Enter a number:\n"""))

if number == 1 or number == 2 :
    if number == 1:
        length = int(input("enter the length of the square :\n"))
        print("the area is : ", length**2)
    else :
        base = int(input("enter the base of the triangle :\n"))
        height = int(input("enter the height of the triangle :\n"))
        result = base*height/2
        print("the area is : ", result)
else :
    print("error: please enter 1 or 2 ")