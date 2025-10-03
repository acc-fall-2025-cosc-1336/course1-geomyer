#create and display a simple menu 
print("Menu:")
print("1. Convert numeric grade to letter grade")
print("2. Exit")

choice = input("Enter your choice (1-2): ")

def number_to_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if choice == "1":
    score = float(input("Enter the numeric grade: "))
    print("Letter grade:", number_to_letter_grade(score))
elif choice == "2":
    print("Exiting the program.")
else:
    print("Invalid choice. Please select 1 or 2.")  