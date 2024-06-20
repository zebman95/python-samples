# show how a change can be uploaded to git
loan_pay = float(input("enter your monthly loan cost: "))
insurance = float(input("enter your monthly insurance cost: "))
gas = float(input("enter your monthly gas cost: "))
oil = float(input("enter your monthly oil cost: "))
tires = float(input("enter your monthly tire cost: "))
maintenance = float(input("enter your monthly maintenance cost: "))

total_monthly = loan_pay + insurance + gas + oil + tires + maintenance
total_annual = total_monthly * 12.0

print("total monthly costs: $"+str(total_monthly))
print("total annual costs:  $"+ str(total_annual))
