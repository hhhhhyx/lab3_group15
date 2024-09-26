slide1=int(input("please input the length of slide1:\n"))
slide2=int(input("please input the length of slide2:\n"))
slide3=int(input("please input the length of slide3:\n"))

if slide1+slide2>slide3 and slide2+slide3>slide1 and slide1+slide3>slide2 :
    if slide1 == slide2 and slide2 == slide3 and slide1 == slide3:
        print("it's an equilateral triangle ")
    elif slide1 == slide2 or slide2 == slide3 or slide1 == slide3:
        print("it's an isosceles triangle ")
    else :
        print("it's a normal triangle ")
else :
    print("it's not a triangle ")