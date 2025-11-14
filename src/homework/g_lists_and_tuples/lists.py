#Homework 8. get_p_distance with list parameter list1 and list2. No magic loops.

def get_p_distance(list1, list2, p):
    """Calculate the p-distance between two lists. 
    The p-distance is defined as the number of positions at which the corresponding elements are different,
    divided by the total number of elements.
    Args:
        list1 (list): ['T','T','T','C','C','A','T','T','T','A']
        list2 (list): ['G','A','T','T','C','A','T','T','T','C']
        list3 (list): ['T','T','T','C','C','A','T','T','T','T']
        list4 (list): ['G','T','T','C','C','A','T','T','T','A']
        p (int): The power to which the differences are raised.
    Returns:
        float: The p-distance between the two lists.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    
    differences = sum(abs(a - b) ** p for a, b in zip(list1, list2))
    p_distance = (differences / len(list1)) ** (1/p)
    
    return p_distance

def get_p_distance_matrix(matrix1, matrix2, p):
    """Calculate the p-distance between two matrices.
    Args:
        matrix1 (list of lists): First matrix.
        matrix2 (list of lists): Second matrix.
        p (int): The power to which the differences are raised.
    Returns:
        float: The p-distance between the two matrices.
    """
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("Matrices must be of the same dimensions")
    
    total_differences = 0
    total_elements = 0
    
    for row1, row2 in zip(matrix1, matrix2):
        for a, b in zip(row1, row2):
            total_differences += abs(a - b) ** p
            total_elements += 1
    
    p_distance = (total_differences / total_elements) ** (1/p)
    
    return p_distance


