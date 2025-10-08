#Function to create a payroll check
#Named Constants to represent the base_hours and the overtime multiplier
HOURS = 40
OVERTIME_MULTIPLIER = 1.5
Rate = 0.0



#Get the gross pay from the hours worked and the hourly rate
def get_gross_pay(hours, rate):
    if hours <= HOURS:
        gross_pay = hours * rate
    else:
        overtime_hours = hours - HOURS
        gross_pay = (HOURS * rate) + (overtime_hours * rate * OVERTIME_MULTIPLIER)
    return gross_pay

def get_fica_tax(gross_pay):
    fica_tax = gross_pay * 0.23
    return fica_tax

def get_federal_tax(gross_pay):
    federal_tax = gross_pay * 0.15
    return federal_tax






#Get the hours worked and the hourly rate from the user
def main():
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate of pay: "))
    #Call the function to calculate the gross pay
    gross_pay = calculate_pay(hours, rate)
    #Display the gross pay
    print(f"The gross pay is: ${gross_pay:.2f}")
