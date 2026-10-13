n = int(input())
inflow = list(map(int, input().split()))
total = 0
min = 0
for i in range(n):
    total +=inflow[i]
    if total > 1000:
        print(i+1)
        break
