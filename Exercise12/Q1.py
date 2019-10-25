#!/usr/bin/python3
import os
import sys

data1 = open("data.csv").read().split('\n')
data1.remove('')

print("Genes for species")
for line in data1:
	line_sep = line.split(",")

	if line_sep[0] == "Drosophila melanogaster" or "Drosophila simulans" and len(line_sep) == 4:
		print(line_sep[2])



print()
print("Genes that length between 90 and 110 bases")
for line in data1:
	line_sep = line.split(",")
	if len(line_sep[1])>=90 and len(line_sep[1])<= 110 and len(line_sep) == 4:
		print(line_sep[2])
	
print()
print("Genes that AT content is less than 0.5")
for line in data1:
	line_sep = line.split(",")
	AT = (line_sep[1].count("A") + line_sep[1].count("T")) / len(line_sep[1])
	if AT < 0.5 and int(line_sep[3]) > 200 and len(line_sep) == 4:
		 print(line_sep[2])

print()
print("Genes for Q4")
for line in data1:
	line_sep = line.split(",")
	if line_sep[2][0] == "k" or line_sep[2][0] == "h" and line_sep[0] != "Drosophila melanogaster" and len(line_sep) == 4:
		print(line_sep[2])
