#Calculate payroll functions

from homework.e_functions.value_return import get_gross_pay, get_fica_tax, get_federal_tax
from homework.e_functions.void_func import display_payroll_check

def calculate_pay(hours, rate):
    gross_pay = get_gross_pay(hours, rate)
    fica_tax = get_fica_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay)
    display_payroll_check(gross_pay, fica_tax, federal_tax)
    return gross_pay

#Main function to get user input and call the calculate_pay function
def main():
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate of pay: "))
    calculate_pay(hours, rate)
    print("Payroll check displayed.")
