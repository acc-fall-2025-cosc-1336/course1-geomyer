# Display menu options

def display_menu():
    print("1. Letter Grade ")
    print("2. Letter Grade Converter with Error Handling")
    print("3. Exit")    
def run_menu():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            from decisions import get_letter_grade
            result = get_letter_grade()
            print(f"Letter Grade: {result}")
        elif choice == '2':
            from decisions import get_letter_grade
            result = get_letter_grade()
            print(f"Letter Grade: {result}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")






        
