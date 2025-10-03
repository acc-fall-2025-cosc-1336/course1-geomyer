#Create function named get_factorial that takes one parameter n

def get_factorial(n):
    #Create a variable named factorial and set it to 1
    factorial = 1
    #Create a for loop that loops through the range of n + 1
    for i in range(1, n + 1):
        #Set factorial to factorial times i
        factorial *= i
    #Return factorial
    return factorial
# Create function named sum_odd_numbers that takes one parameter n
def sum_odd_numbers(n):
    #Create a variable named total and set it to 0
    total = 0
    #Create a for loop that loops through the range of n + 1
    for i in range(n + 1):
        #If i modulo 2 is not equal to 0
        if i % 2 != 0:
            #Set total to total plus i
            total += i
    #Return total
    return total

#Create a menu named d_repetition

