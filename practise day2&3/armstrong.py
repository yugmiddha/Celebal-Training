number = int(input())
temp = number
n = len(str(number))
while temp > 0:
    digit = temp % 10
    armstrong = digit ** n
    temp //= 10
if armstrong == number:
    print("armstrong")
else:
    print("not armstrong")

