first_name = input("enter your first name:\n")

if len(first_name)<5 :
    surname = input("enter your surname:\n")
    fullname = first_name+surname
    result = str.upper(fullname)
    print("the fullname is : ",result)
else :
    print("the first name is: ",first_name)