def dna_to_rna(dna):
    return dna.replace('T', 'U')


dna_strand = "GCAT"
rna_strand = dna_to_rna(dna_strand)
print(rna_strand)  
