#!/usr/bin/python3
import os
import sys

input_txt_contents = open('input.txt').read().upper().split()
cleanseqs = open('Cleaned_sequences.txt','w')
for cleanones in input_txt_contents:
	cleanseqs.write(cleanones[14:] + '\n')
	cleanones[14:]
cleanseqs.close()
print(open('Cleaned_sequences.txt').read().rstrip())
