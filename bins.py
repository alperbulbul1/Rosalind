n,m,x,y = open("rosalind_bins.txt").read().strip().split("\n")

n = int(n)
m = int(m)
x = [int(i) for i in x.split()]

y = [int(i) for i in y.split()]

#
#q = [10, 20, 30, 40, 50]
#w = [40, 10, 35, 15, 40, 20]


def binary_se(list_it, it, out=[]):
    first = 0
    last = len(list_it) -1
    found = False
    while not found and first <= last:
        mid = (last + first) // 2

        if list_it[mid] == it:
            out.append(mid+1)
            found = True
        else:
            if it < list_it[mid]:
                last = mid -1

            elif it > list_it[mid]:
                first = mid +1
    if found == False:
        out.append(-1)
    return out

z = []
for i in y:
    z = binary_se(x, i)

print(z)
fw = open("bins-out.txt","w")
for i in z:
    fw.write(str(i))
    fw.write(" ")
