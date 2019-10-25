#! /user/bin/python3

dna = "ATGCATCATG"
k=2 
n=2

def kmer(dna,k,n):
	len_dna = len(dna)-k
	list = []
	for x in range(len_dna):
		seq = dna[x:x+k]
		if dna.count(seq) > n and (seq not in list):
			print(seq)
			list.append(seq)

kmer(dna,k,n)

def similarity(dna1,dna2):
	length = min(len(dna1),len(dna2))
	common = 0
	for x in range(length):
		if dna1[x] == dna2[x]:
			common += 1
	return common/length

print(similarity('ATTGTACGG', 'AATGAACCG'))
