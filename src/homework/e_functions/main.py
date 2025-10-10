#Get the hours worked and the hourly rate from the user
def calculate_pay(hours, rate):
    return hours * rate

def main():
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate of pay: "))
    #Call the function to calculate the gross pay
    gross_pay = calculate_pay(hours, rate)
    #Display the gross pay
    print(f"Gross Pay: ${gross_pay:.2f}")
    return gross_pay

if __name__ == "__main__":
    main()