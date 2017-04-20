with open('rosalind_rna.txt', 'r') as f:
    DNA = f.read()

def convDNA2RNA(data):
    return data.replace('T', 'U')

ans = convDNA2RNA(DNA)
print ans
