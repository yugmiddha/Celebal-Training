Balance = int(input("Enter the balance:"))
n = int(input("Enter the request:"))
for _ in range(n):
    amount = int(input("Enter the amount to withdraw:"))
    if amount > 0 and amount %100 == 0 and amount <= Balance:
        Balance -= amount
        print("successful")
    else:
        print("failed")