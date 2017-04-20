with open('rosalind_dna.txt', 'r') as f:
    data = f.read()

def cnt(data):
    return data.count('A'), data.count('C'), data.count('G'), data.count('T')
cnt(data)
