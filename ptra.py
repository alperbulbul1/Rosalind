from Bio.Seq import translate, Seq


def ptra(dna, protein):

    for i in range(1, 15):
        trans = translate(dna, stop_symbol="", table=i)
        if trans == protein:
            return i


if __name__ == '__main__':
    dna, protein = open('rosalind_ptra.txt').read().strip().split('\n')
    print(ptra(dna, protein))
