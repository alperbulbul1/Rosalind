def count_patt(t, p):
    count = 0
    for i in range(len(t)-len(p)+1):
        if (t[i:i+len(p)] == p):
            count += 1

    print(count)


f = open("rosalind_ba1a.txt", "r")
text = ""
pattern = ""
lines =f.readlines()
text = lines[0].split()
pattern = lines[1].split()

count_patt(text[0], pattern[0])
