num = int(input())
rev = 0
orignal = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if orignal == rev:
    print("palindrome")
else:
    print("not palindrome")