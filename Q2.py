dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
dna_comp = ''
for x in dna:
	if x == 'A':
		dna_comp += 'T'
	elif x == 'T':
		dna_comp += 'A'
	elif x == 'C':
		dna_comp += 'G'
	elif x == 'G':
		dna_comp += 'C'
print (dna_comp)
