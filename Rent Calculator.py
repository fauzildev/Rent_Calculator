## input needed
# Total Hostel Rent
# Tital Food Ordered
# Electricity Units Spends
# Charger Per Unit

## Output
# Total Amount every person have to pay is

Rent=int(input("Enter Hostel You Rent:"))
Food=int(input("Enter Amount of Food You Ordered:"))
Electricity_Spends=int(input("Enter Total of Electricity Spends:"))
Charger_Per_Unit=int(input("Enter The Charger Per Unit:"))
Persons=int(input("Enter the number of persons living in room:"))

Total_Bill= Electricity_Spends * Charger_Per_Unit
Total_Cost= Food + Total_Bill + Rent
output= Total_Cost // Persons

print("=====BILL SUMMARY=====")
print(f"Total Rent =Rp{Rent:,}")
print(f"Total Food =Rp{Food:,}")
print(f"Total Electricity Bill =Rp{Electricity_Spends:,}")
print("----------------------")
print(f"Total Cost =Rp{Total_Cost:,}")
print(f"Each Person Pays =Rp{output:,.2f}")
