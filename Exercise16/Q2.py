import numpy as np
import matplotlib.pyplot as plt
import os,sys

aln = open("/localdisk/data/BPSM/Lecture16_AI/alignment.txt")
aligned_seqs = []

for line in aln:
	aligned_seqs.append(line.rstrip("\n"))

alignment_length = len(aligned_seqs[0])
uniques_per_column = []

for column_number in range(alignment_length):
    column = []
    for seq in aligned_seqs:
        aa = seq[column_number]
        if aa != '-':  # ignore gaps
            column.append(seq[column_number])
    uniques = len(set(column))
    uniques_per_column.append(uniques)

window = 10
numbers_to_plot = []
for start in range(len(uniques_per_column) - window):
    win = uniques_per_column[start:start+window]
    score = sum(win) / len(win)
    numbers_to_plot.append(score)

plt.figure(figsize=(15,8))
plt.xlim(0,len(numbers_to_plot))
plt.plot(numbers_to_plot,linewidth=3,color="green")
plt.title('EXERCISE 2')
plt.ylabel('Unique amino acid residues')
plt.xlabel('Residue position')
plt.savefig("Lecture16_Exercise_2.png",transparent=True)
plt.show()
