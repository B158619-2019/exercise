def percentage(dna, amino_acid = []):
	amount = 0
	if amino_acid != []:
		for aa in dna:
			for amino in amino_acid:
				if aa == amino:
					amount += 1
		return amount/len(dna)*100
	else:
		for aa in dna:
			if aa in ["A","I","L","M","F","W","Y","V"]:
				amount += 1
		return amount/len(dna)*100


assert round(percentage("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(percentage("MSRSLLLRFLLFLLLLPPLP")) == 65
