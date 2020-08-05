def kmp(s):
    def longest_substring(k,bound):
        for j in range(k-bound,k):
            if k-j<=bound:
                if s[j:k]==s[0:k-j]:
                    return k-j
        return 0
 
    result=[]
    longest=-1
    for k in range(1,len(s)+1):
        longest=longest_substring(k,longest+1)
        result.append(longest)
    return result

if __name__=='__main__':
    name=''
    strings=[]
    with open('rosalind_kmp.txt') as f:
        for line in f:
            if (len(name))==0:
                name=line.strip()
            else:
                strings.append(line.strip())
    string=''.join(s for s in strings)

    print(' '.join(str(i) for i in kmp(string)))
    a = ' '.join(str(i) for i in kmp(string))

    fw = open("kmp-out.txt", "w")
    fw.write(a)
