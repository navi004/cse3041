#Chocolate Bob
money = int(input("Enter money:"))
price = int(input("Enter price :"))
discount = int(input("Enter M :"))
bought = money//price
total = bought + bought//discount
print("Total chocolates :",total)
