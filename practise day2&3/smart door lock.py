passw = input().strip()
attempts = [input().strip() for _ in range(3)]
for pin in attempts:
    if passw == pin:
        print("Access Granted")
        break
else:
     print("Access Denied") 





