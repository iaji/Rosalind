with open('rosalind_revc.txt', 'r' ) as f:
    DNA = f.read()

RevDNA = DNA[::-1]
finalDNA = ''
#def compDNA(data):
for part in RevDNA:
    if part == 'T':
        #finalDNA.append('A')
        finalDNA += 'A'
    elif part == 'A':
        finalDNA += 'T'
    elif part == 'C':
        finalDNA += 'G'
    elif part == 'G':
        finalDNA += 'C'
print(finalDNA)
