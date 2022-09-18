
## FUNCTION TO FIND HOW MUCH YOU SAVE GIVEN AN ANUAL SALARY AND % SAVED
def months_to_save(annual_salary, portion_saved):      
    
    semi_annual_raise = 0.07
    salary = annual_salary / 12
    months_to_save = 0
    current_savings = 0
    r_anual = 0.04
    r_monthly = r_anual / 12
    
    while months_to_save < 36:
        current_savings *= (1 + r_monthly)
        current_savings += salary * portion_saved
        months_to_save += 1
        if months_to_save % 6 == 0:
            salary *= (1+ semi_annual_raise)
            
    return current_savings
  

## TOTAL COST OF THE HOUSE    
total_cost = 1000000  
portion_down_payment = total_cost * 0.25     


percents = list(range(0,10000))
low = 0
high = len(percents)
mid = (high + low) // 2

anual_salary = 300000
percentage = percents[mid] / 10000
saved = months_to_save(anual_salary, percents[mid] / 10000)
steps = 1
diff = saved - portion_down_payment


while abs(diff) > 100:
    steps += 1
    if  saved > portion_down_payment:
        high = mid
        mid = (high + low) // 2
        percentage = percents[mid] / 10000
        saved = months_to_save(anual_salary, percentage)
        diff = saved - portion_down_payment
        #print("elif",percentage,diff)
    else:
        low = mid
        mid = (high + low) // 2
        percentage = percents[mid] / 10000
        saved = months_to_save(anual_salary, percentage)
        diff = saved - portion_down_payment
        #print("else",percentage,diff)

print("Percentage needed: ", percentage, "Steps to discover: ", steps)
        

    