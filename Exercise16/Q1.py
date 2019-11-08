import numpy as np
import matplotlib.pyplot as plt
import os,sys

ecoli = open("/localdisk/data/BPSM/Lecture16_AI/ecoli.txt").read().replace('\n', '').upper()[0:100000]
window = 1000
at = []
counter = 0
for start in range(len(ecoli)-window):
	counter += 1
	win = ecoli[start: start+window]
	at.append( (win.count('A')+win.count('T')) / window)

plt.figure(figsize=(20,10))
plt.plot(at, label="AT content",linewidth=3,color="purple")
plt.ylabel('Fraction of bases')
plt.xlabel('Position on genome')
plt.title("EXERCISE 1\nAT content, 1kb windows of the E.coli genome")
plt.legend()
plt.savefig("Lecture16_Exercise_1.png",transparent=True)
plt.show()
