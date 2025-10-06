#HomeWork 4 Menu

from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def factorial(n):
    """Calculates the factorial of a given number."""
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def sum_odd_numbers(n):
    """Calculates the sum of odd numbers up to a given number."""
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("\n--- Homework 4 Menu ---")
        print("1- Factorial")
        print("2- Sum odd numbers")
        print("3- Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                try:
                    num = int(input("Enter a number (greater than 0 and less than 10): "))
                    if 0 < num < 10:
                        print(f"The factorial of {num} is: {factorial(num)}")
                        break
                    else:
                        print("Invalid input. Number must be greater than 0 and less than 10.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        elif choice == '2':
            while True:
                try:
                    num = int(input("Enter a number (greater than 0 and less than 100): "))
                    if 0 < num < 100:
                        print(f"The sum of odd numbers up to {num} is: {sum_odd_numbers(num)}")
                        break
                    else:
                        print("Invalid input. Number must be greater than 0 and less than 100.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
if __name__ == "__main__":
    main_menu()