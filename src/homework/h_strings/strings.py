#Calculates the Hamming distance between two DNA strings without string slicing.
def hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings must be of equal length.")
    
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
            
    return distance
# Example Usage
dna_string1 = "GAGCCTACTAACGGGAT"
dna_string2 = "CATCGTAATGACGGCCT"
print(hamming_distance(dna_string1, dna_string2))

# Get DNA complement without string slicing

def get_dna_complement(dna):
    complement = ""
    for nucleotide in dna:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'
        else:
            raise ValueError("Invalid nucleotide found: " + nucleotide)
    return complement

# Example usage:
dna_sequence = "AAAACCCGGT"
complementary_sequence = get_dna_complement(dna_sequence)
print(f"Original DNA sequence: {dna_sequence}")
print(f"Complementary sequence: {complementary_sequence}")