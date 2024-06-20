def calculateStateSalesTax(amt):
   return amt * 0.05;

def calculateCountyTax(amt):
   return amt * 0.025;

def calculateTotalSalesTax(amt):
   print("total tax: "+str(0.05+0.025))
   return amt * (0.05 + 0.025);


amount = input("Enter amount of a purchase: ")

print("amount of purchase: "+amount)
stateTax = calculateStateSalesTax(float(amount))
countyTax = calculateCountyTax(float(amount))
totalTax = calculateTotalSalesTax(float(amount))
totalAmount = float(amount) + totalTax;

print("state sales tax of amount: "+str(stateTax))
print("county sales tax of amount: "+str(countyTax))
print("total sales tax of amount: "+str(totalTax))
print("total of the sale: "+str(totalAmount))

