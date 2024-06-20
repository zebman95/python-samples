land_value = float(input("enter the land value: "))

assessment = land_value * 0.60
property_tax = (assessment/100.0) * 0.72

print("assessment value: $"+str(assessment))
print("property tax:     $"+str(property_tax))
