def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length to calculate distance.")
    
    distance = 0
    for a, b in zip(list1, list2):
        if a != b:
            distance += 1
    return distance / len(list1)
# Assuming the following lists exist
list1 = ['T','T','T','C','C','A','T','T','T','A']
list2 = ['G','A','T','T','C','A','T','T','T','C']
list3 = ['T','T','T','C','C','A','T','T','T','T']
list4 = ['G','T','T','C','C','A','T','T','T','A']

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

lists_to_compare = [list1, list2, list3, list4]
list_to_compare = [list2, list1, list3, list4]  # Reordered as per the test case
p_distance_matrix = get_p_distance_matrix(lists_to_compare)

print("The p-distance matrix is:")
for row in p_distance_matrix:
    print([round(val, 2) for val in row])




