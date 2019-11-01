gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def translation_sub(dna):
	protein = ''
	while len(dna) >= 3:
		protein += gencode[dna[0:3]]
		dna = dna[1:]
		dna = dna[1:]
		dna = dna[1:]
	return protein

def translation(dna):
	dna_copy = dna
	protein1 = translation_sub(dna_copy)
	dna_copy = dna_copy[1:]
	protein2 = translation_sub(dna_copy)
	dna_copy = dna_copy[1:]
	protein3 = translation_sub(dna_copy)

	reverse = {'A':'T','C':'G','T':'A','G':'C'}
	dna_reverse = ''
	for aa in dna:
		dna_reverse += reverse[aa]
	protein_reverse1 = translation_sub(dna_reverse)
	dna_reverse = dna_reverse[1:]
	protein_reverse2 = translation_sub(dna_reverse)
	dna_reverse = dna_reverse[1:]
	protein_reverse3 = translation_sub(dna_reverse)

	print(protein1)
	print(protein2)
	print(protein3)
	print(protein_reverse1)
	print(protein_reverse2)
	print(protein_reverse3)

dna = 'ATATATATAT'
translation(dna)


