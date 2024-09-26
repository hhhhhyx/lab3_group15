is_raining = input("is it raining? ")
is_raining = str.lower(is_raining)

if is_raining == "yes" :
    windy = input("is it windy? ")
    windy = str.lower(windy)
    if windy == "yes":
        print("it's too windy for an umbrella")
    else :
        print("take an umbrella")
else:
    print("enjoy your day")