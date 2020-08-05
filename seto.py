#f = open("rosalind_seto.txt", "r")
#n = f.readline()
#a = f.readline()
#b = f.readline()
#a = set(a.split())
#b = set(b.split())
#n = int(n)
#un = a.union(b)
#inter = a.intersection(b)
#adif = a.difference(b)
#bdif = b.difference(a)
#acomp = []
#
#for i in range(1, n+1):
#    if i not in a:
#        acomp.append(i)
#
#acomp = set(acomp)
#bcomp = []
#for x in range(1,n+1):
#	if x not in b:
#		bcomp.append(x)
#bcomp = set(bcomp)
#
# 
#print(un)
#print(inter)
#print(adif)
#print(bdif)
#print(acomp)
#print(bcomp)




with open('rosalind_seto.txt') as input_data:
	S, A, B = input_data.readlines()
	# Convert to sets.
	S = set( [i for i in range(1,int(S.strip())+1)] )
	A = set(map(int, A.strip().rstrip('}').lstrip('{').replace(' ', '').split(',')))
	B = set(map(int, B.strip().rstrip('}').lstrip('{').replace(' ', '').split(',')))

with open('051_SETO.txt', 'w') as output_data:
	# A union B
	output_data.write('{'+', '.join(map(str,list(A|B)))+'}'+'\n')
	# A interset B
	output_data.write('{'+', '.join(map(str,list(A&B)))+'}'+'\n')
	# A - B
	output_data.write('{'+', '.join(map(str,list(A-B)))+'}'+'\n')
	# B - A
	output_data.write('{'+', '.join(map(str,list(B-A)))+'}'+'\n')
	# A Complement
	output_data.write('{'+', '.join(map(str,list(S-A)))+'}'+'\n')
	# B Complement
	output_data.write('{'+', '.join(map(str,list(S-B)))+'}')
