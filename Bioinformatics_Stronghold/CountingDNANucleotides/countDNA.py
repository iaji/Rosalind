with open('rosalind_dna.txt', 'r') as f:
    data = f.read()

A = 0
C = 0
G = 0
T = 0

for nucelotide in data:
    if nucelotide == 'A':
        A += 1
    elif nucelotide == 'C':
        C += 1
    elif nucelotide == 'G':
        G += 1
    elif nucelotide == 'T':
        T += 1
    else:
        print(nucelotide)

result = [A, C, G, T]

print result
