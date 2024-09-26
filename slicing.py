lyrics = input("what's your favorite song? ")
length = len(lyrics)
print("this has",length,"letters")
start_number = int(input("input the starting number:"))
ending_number = int(input("input the ending nunmber:"))
part = (lyrics[start_number:ending_number])

print("the section of the text:",part)