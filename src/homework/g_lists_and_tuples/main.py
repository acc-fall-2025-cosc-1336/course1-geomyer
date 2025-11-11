#
#Test Menu for to show the list of lowest and high values from a list
from unittest.main import main
from lists import get_lowest_values, get_highest_values


# Menu of lowest and highest values. Prompt user for input Options: 1. Get lowest and highest values from the list 2. Exit
def display_menu(lowest, highest):  
    while True:
        print("Menu")
        print("1. Get lowest and highest values from the list")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")
        if choice == '1':
            print(f"The lowest values are: {lowest}")
            print(f"The highest values are: {highest}")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    input_list = [8, 10, 1, 50, 20]
    n_lowest = 3
    n_highest = 2
    lowest_values = get_lowest_values(input_list, n_lowest)
    highest_values = get_highest_values(input_list, n_highest)
    display_menu(lowest_values, highest_values)
if __name__ == "__main__":
    main()  
