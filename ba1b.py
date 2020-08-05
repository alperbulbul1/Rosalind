import  numpy as np
def kmer_find(t, k):
    count = 0
    maxf = 0
    indi = np.zeros(len(t))
    mostk = set()
    p = []
    for i in range(len(t)-k):
        p.append(t[i:i+k])

    for i in range(len(t)-k):
        for j in p:
            if t[i:i+len(j)] == j:
                 count += 1
        indi[i] = count
    maxf = indi.max()
    for i in range(len(t)-k):
        if indi[i] == maxf:
            mostk.add(t[i:i+k])

    print(mostk)
        
def fasterMostFrequentsKMers(text, k, frequency=-1):

    textLen = len(text)
    frequencyArray = dict()
    mostFrequentPatterns = []

    for i in range(0, textLen - k):
        try:
            frequencyArray[text[i:i+k]]+=1
        except KeyError as err:
            frequencyArray[text[i:i+k]] = 1

    frequency = max(frequencyArray.values()) if frequency < 0 else frequency

    for key in frequencyArray.keys():
        if frequencyArray[key] >= frequency:
            mostFrequentPatterns.append(key)

    return mostFrequentPatterns    


f = open("rosalind_ba1b.txt","r")

text = f.readline()

k = int(f.readline())

kmer_most = fasterMostFrequentsKMers(text,k)
for i in kmer_most:
    print(i)
         
