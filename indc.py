from numpy import log10
from scipy.special import comb

n = 47 

common_alg = [log10(comb(2 * n, i)) + i * log10(0.5) + (2 * n - i) * log10(0.5) for i in range(n * 2 + 1)]
prob = [10 ** x for x in common_alg]
probabilities = [0 for _ in prob]
    
for i in range(n*2, -1, -1):
    probabilities[i] = log10(sum([prob[j] for j in range(i, n*2 + 1)]))


print(" ".join([str(x) for x in probabilities[1:]]))
