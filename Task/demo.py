hours_worked = 50
pay_rate = 7.25
overtime_rate = 1.5
work_hours_in_week = 40

total_pay = hours_worked * pay_rate

print(total_pay)

if(hours_worked <= work_hours_in_week):
   total_pay
   print(total_pay)
elif(hours_worked > work_hours_in_week):
   overtime_hours = hours_worked - work_hours_in_week
   over_total_pay = total_pay + (overtime_hours * pay_rate * overtime_rate)
   print(over_total_pay)
else:
    print("Out of Range")