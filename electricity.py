# Electricity Bill Calculation
units = int(input("Enter number of units consumed: "))
bill = 0

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3
else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

print("Total electricity bill: ₹", bill)

print("SOME CHANGES")
