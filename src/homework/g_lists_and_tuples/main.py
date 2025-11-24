#HW 8 Get P-Distance_Matrix

def get_p_distance(list1, list2):
    """
    Compute the p-distance (proportion of differing positions) between two lists.
    Raises ValueError if the lists have different lengths.
    """
    if len(list1) != len(list2):
        raise ValueError("Sequences must be the same length to compute p-distance")
    if len(list1) == 0:
        return 0.0
    mismatches = 0
    for a, b in zip(list1, list2):
        if a != b:
            mismatches += 1
    return mismatches / len(list1)

def get_p_distance_matrix(list_of_lists):
    """
    Build a matrix of pairwise p-distances between lists using get_p_distance.
    """
    n = len(list_of_lists)
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0.0
            else:
                matrix[i][j] = get_p_distance(list_of_lists[i], list_of_lists[j])
    return matrix
lists_to_compare = []
#Example usage: 
list1 = ['T','T','T','C','C','A','T','T','T','A']
list2 = ['G','A','T','T','C','A','T','T','T','C']
list3 = ['T','T','T','C','C','A','T','T','T','T']
list4 = ['G','T','T','C','C','A','T','T','T','A']
lists_to_compare = [list1, list2, list3, list4]
p_distance_matrix = get_p_distance_matrix(lists_to_compare)
print("The p-distance matrix is:")
for row in p_distance_matrix:
    print([round(val, 2) for val in row])

#Create the following menu.
#Menu Options:
#1-Get P-Distance Matrix
#2-Exit
#The program runs until the user chooses option 2
# Assuming the following lists exist
list1 = ['T','T','T','C','C','A','T','T','T','A']
list2 = ['G','A','T','T','C','A','T','T','T','C']
list3 = ['T','T','T','C','C','A','T','T','T','T']
list4 = ['G','T','T','C','C','A','T','T','T','A']

while True:
    print("Menu Options:")
    print("1-Get P-Distance Matrix")
    print("2-Exit")
    choice = input("Please enter your choice (1 or 2): ")
   #Option 1 prompt the user for a list, call the get_p_distance_matrix function and display the result 
    if choice == '1':
        num_lists = int(input("Enter the number of lists to compare: "))
        lists_to_compare = []
        for i in range(num_lists):
            user_list = input(f"Enter list {i+1} elements separated by commas: ")
            user_list = user_list.split(',')
            lists_to_compare.append(user_list)

        p_distance_matrix = get_p_distance_matrix(lists_to_compare)
        print("The p-distance matrix is:")
        for row in p_distance_matrix:
         print([round(val, 2) for val in row])
    elif choice == '2':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
