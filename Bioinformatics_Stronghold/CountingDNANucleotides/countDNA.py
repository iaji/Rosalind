with open('rosalind_dna.txt', 'r') as f:
    data = f.read()
result = [A, C, G, T]
A = 0
C = 1
G = 2
T = 3
for nucelotide in data:
    if nucelotide == 'A':
        result[0] += 1
    elif nucelotide == 'C':
        result[1] += 1
    elif nucelotide == 'G':
        result[2] += 1
    elif nucelotide == 'T':
        result[3] += 1

print result
