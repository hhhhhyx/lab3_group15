number_of_sides = int(input("please input the number of sides: \n"))


def match_shape(numbers):
    match numbers:
        case 3:
            print("it's triangle")
        case 4:
            print("it's quadrilateral")
        case 5:
            print("it's pentagon")
        case 6:
            print("it's hexagon")
        case 7:
            print("it's heptagon")
        case 8:
            print("it's octagon")
        case 9:
            print("it's nonagon")
        case 10:
            print("it's decagon")

if number_of_sides >= 3 and number_of_sides <= 10 :
    match_shape(number_of_sides)
else :
    print("An appropriate error message ")