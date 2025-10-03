#function to convert a numerical grade to a letter grade

def get_letter_grade():
    '''Prompts the user for a number grade and returns the corresponding letter grade.'''
    try:
        grade = float(input("Enter the number grade (0-100): "))
        if 0 <= grade <= 100:
            letter_grade = number_to_letter_grade(grade)
            return letter_grade
        else:
            return "Error: Grade must be between 0 and 100."
    except ValueError:
        return "Error: Invalid input. Please enter a numeric value."
def number_to_letter_grade(grade):
    '''Converts a numeric grade to a letter grade.'''
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    elif grade >= 0:
        return 'F'
    


