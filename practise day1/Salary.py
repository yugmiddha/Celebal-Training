salary = float(input("Enter the salary: "))
late_days = int(input("Enter the number of late days: "))
absent_days = int(input("Enter the number of absent days: "))
if(late_days > 10):
    late_deduction = 0.10
elif(late_days > 5):
    late_deduction = 0.05
else:
    late_deduction = 0
if(absent_days > 2):
    absent_deduction = 0.05
else:
    absent_deduction = 0
total_deduction = late_deduction + absent_deduction
final_salary = salary - (salary * total_deduction)
print("The final salary is:", final_salary)
