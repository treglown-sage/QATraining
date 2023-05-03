personal_allowance = 11850

def tax_calculator(pay, percentage):
    return (pay * percentage) / 100

def getIncomeTax(income: float)->float:
    if income <= personal_allowance:
        return tax_calculator (income, 0)
    elif  income > personal_allowance and income <34500:
        return tax_calculator (income - personal_allowance, 20) 
    elif income > 34500 and income < 150000:
        return tax_calculator(income - personal_allowance, 40) 
    elif income > 150000:
        return tax_calculator(income - personal_allowance, 45) 
    else:
        print("You must input your annual income!")

income = float(input("Input your annual income: £"))
calculated_tax = getIncomeTax(income) 
print(f"Your annual tax is £{calculated_tax} with income of {income}")  
