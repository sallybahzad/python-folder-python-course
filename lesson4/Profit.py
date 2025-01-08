actual_cost=float(input("pls. enter the actual product price "))
sale_amount=float(input("pls. enter the actual sale amount "))
if(sale_amount>actual_cost):
    amount=sale_amount-actual_cost
    print("total profit= ",amount)
else:
    print("no profit")
    