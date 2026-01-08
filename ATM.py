# ATM Withdrawal System

balance = 10000  # initial balance

withdraw = int(input("Enter withdrawal amount: "))

if withdraw % 100 != 0:
    print("Amount must be a multiple of 100")
elif withdraw > balance:
    print("Insufficient balance")
else:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Updated balance:", balance)
print("Changes in ATM Code")
print("dev-electricity")
print("dev-atm")