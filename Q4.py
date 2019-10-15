dna = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'
print (dna[:63],dna[90:])
print ('The percentage of the coding sequence is', (len(dna)-27)/len(dna)*100)
a = dna[63:90].lower()
print (dna[:63]+a+dna[90:])
