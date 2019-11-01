#!/usr/bin/python3
import os
import sys

genomic = open('genomic_dna2.txt').read()
exons = open('exons.txt').read().replace(',','\n').split()
output= ''
fullcoding = open('Exercise2_coding_seqence.fasta','w')
for x in range(len(exons)):
	if x%2 ==0:
		fullcoding.write(genomic[int(exons[x]),int(exons[x+1])]+'\n')
fullcoding.close()
print(open('Exercise2_coding_seqence.fasta').read())

	
