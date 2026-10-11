password = input("Enter the password: ")
digit = False
upper = False
for char in password:
    if char.isdigit():
        digit = True
    if char.isupper():
        upper = True


if len(password) >= 8 and digit and upper:
        print("Strong")
else:
        print("Weak")