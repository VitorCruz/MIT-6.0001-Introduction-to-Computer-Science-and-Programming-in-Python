
annual_salary =  int(input("Your anual salary: "))
portion_saved = float(input("Portion of salary saved, in decimal: "))
total_cost = int(input("Cost of your dream home: "))

portion_down_payment = total_cost * 0.25
current_savings = 0
r_anual = 0.04
r_monthly = r_anual / 12

months_to_save = 0
while current_savings < portion_down_payment:
    current_savings *= (1 + r_monthly)
    current_savings += annual_salary / 12 * portion_saved
    months_to_save += 1

print("Money obtained:", current_savings)
print("Months to save:", months_to_save)
    
    