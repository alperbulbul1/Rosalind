from Bio import SeqIO

def average(l):
	return sum(l) / float(len(l))


a = []
for record in SeqIO.parse("phre.txt", "fastq"):
    a.append(average(record.letter_annotations["phred_quality"]))

z = 0

for i in a:
    print(i)
    if i < 22:
        z += 1

print(z)

