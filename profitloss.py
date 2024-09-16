cost=float(input("Enter the actual cost:"))
sale=float(input("Enter the price:"))
if sale>cost:
    amount=(sale-cost)
    print("The profit is :", amount)
else:
    print("NO PROFIT!!")    
