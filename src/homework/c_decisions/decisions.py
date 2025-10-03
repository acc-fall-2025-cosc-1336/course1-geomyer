#Write a function for get_letter_grade(score) that takes a numeric score as input and returns the corresponding letter grade based on the following scale:
#90-100: A
#80-89: B
#70-79: C
#60-69: D
#0-59: F
#If the score is outside the range of 0-100, return "Invalid score".
def get_letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
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