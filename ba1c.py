if __name__ == "__main__":
    f = open("rosalind_ba1c.txt","r")
    dna = f.readline()

    ans = ""
    
    for i in reversed(range(len(dna))):
        if dna[i] == 'A':
            ans = ans + 'T'
        elif dna[i] == 'T':
            ans = ans + 'A'
        elif dna[i] == 'C':
            ans = ans + 'G'
        elif dna[i] == 'G':
            ans = ans + 'C'
    
    print(ans)
