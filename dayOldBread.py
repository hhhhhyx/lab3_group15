numbers_of_bread=input("********please input the numbers of loaves of day old bread being purchased\n")
numbers_of_bread = float(numbers_of_bread)
print("DESCRIPTION               PRICE               DISCOUNT          AMOUNT")
day_old_bread_price = 3.49
discount = 0.4
total_amount = float(day_old_bread_price*discount*numbers_of_bread)

#print("DAY OLD BREAD"+"             "+ str("%.2f"%day_old_bread_price)+"                "+ "60% OFF"+"           "+ str("%.2f"%total_amount))

print("DAY OLD BREAD            ", "%.2f"%day_old_bread_price,"               60% OFF          ","%.2f"%total_amount)