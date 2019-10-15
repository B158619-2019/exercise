dna = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
a = dna.find('GAATTC')
print("The lengths of the 2 fragments are", a+1, len(dna)-a-1)
