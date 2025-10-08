#display_payroll_check function 

def display_payroll_check(gross_pay, fica_tax, federal_tax):
    net_pay = gross_pay - fica_tax - federal_tax
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"FICA Tax: ${fica_tax:.2f}")
    print(f"Federal Tax: ${federal_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")


    