from Bio import SeqIO

def revere_comp(dna):
    a = ""

    for s in reversed(dna):
        if s == "A":
            a = a + "T"
        elif s == "T":
            a = a + "A"
        elif s == "G":
            a = a + "C"
        elif s == "C":
            a = a + "G"
    return a

records = SeqIO.parse("rosalind_rvco.txt", "fasta")

z = 0
 
for record in records:

    ans = revere_comp(record.seq)

    if ans == record.seq:
        z += 1

print(z)
    
