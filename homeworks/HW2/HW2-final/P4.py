def dna_complement(dna_input):
    real_dna_character = ['A', 'T', 'C', 'G']
    dna_input_upper = dna_input.upper()

    if dna_input_upper == '':
        print('Your input is None.')
    elif all (character in real_dna_character for character in dna_input_upper):
        #for character in dna_input_upper:
        compliment_dna = dna_input_upper
        compliment_dna = compliment_dna.replace('A', '1')
        compliment_dna = compliment_dna.replace('T', 'A')
        compliment_dna = compliment_dna.replace('1', 'T')
        compliment_dna = compliment_dna.replace('G', '2')
        compliment_dna = compliment_dna.replace('C', 'G')
        compliment_dna = compliment_dna.replace('2', 'C')
        print(compliment_dna)
    else:
        print('Your input is invalid.')
        return None

# test valid input
input_sequence = 'cAagT'
dna_complement(input_sequence)


# test invalid input
print('')
input_sequence = 'chgi12'
print(input_sequence)
output_sequence = dna_complement(input_sequence)

# test None input
print('')
input_sequence = ''
print(input_sequence)
output_sequence = dna_complement(input_sequence)
