# Homework 6 Menu
# Displays the main menu and handles user input for string operations. No slices allowed.

def hamming_distance(str1, str2):
    """Calculate the Hamming distance between two strings."""
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length to calculate Hamming distance.")
    distance = 0
    for a, b in zip(str1, str2):
        if a != b:
            distance += 1
    return distance
def get_dna_complement(dna_strand):
    """Return the DNA complement of a given DNA strand."""
    complement = ''
    for nucleotide in dna_strand:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'
        else:
            raise ValueError("Invalid nucleotide found in DNA strand.")
    return complement
if __name__ == "__main__":
    
    while True:     
        print("\n--- Homework 6 Menu ---")
        print("1- Hamming Distance")
        print("2- DNA Complement")
        print("3- Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            str1 = input("Enter the first string: ")
            str2 = input("Enter the second string: ")
            try:
                distance = hamming_distance(str1, str2)
                print(f"The Hamming distance between the two strings is: {distance}")
            except ValueError as e:
                print(e)
        elif choice == '2':
            dna_strand = input("Enter a DNA strand: ")
            complement = get_dna_complement(dna_strand)
            print(f"The DNA complement of the strand is: {complement}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue
