#Problem 1
#25-07-23 Naveen 22MIA1049
#DA is 80% of basic pay
#HRA is 30% of Basic pay
#deduction in salary of 12% of Basic pay
basic_pay = float(input("Enter Basic Pay : "))
netpay = basic_pay+(basic_pay*0.8)+(basic_pay*0.3)-(basic_pay*.12)
print("Netpay : ",netpay)
