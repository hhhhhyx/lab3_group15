word = input("input a word: ")
first = word[0]
rest = word[1:len(word)-1]
if first!="a" and first!="e" and first!="i" and first!="o" and first!="u" :
    result = rest+first+"ay"
else :
    result = word + "way"
print("the result is: ",result)