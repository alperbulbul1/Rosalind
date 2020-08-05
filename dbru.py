def constructGraph(inputList):
    inputSet = set()
    for item in inputList:
        rev = complement(item)
        inputSet.add(item)
        inputSet.add(rev)
    #Because reads are of equal length
    length = len(inputList[0])
    print(length)
    edgelist =[]
    for item in inputSet:
        left = item[0:length-1]
        right = item[1:length]
        edgelist.append((left,right))

    return edgelist


def complement(read):
    comp = ''
    for i in read:
        if i == 'A':
            comp += 'T'
        if i == 'C':
            comp += 'G'
        if i == 'G':
            comp += 'C'
        if i == 'T':
            comp += 'A'

    return comp[::-1]

file = open("rosalind_dbru.txt")

inputList= file.read().splitlines()

results = constructGraph(inputList)

fw = open("dbru-out.txt", "w")
for j in results:
    string = str(j)
    fw.write(string.replace("'",""))
    fw.write("\n")
