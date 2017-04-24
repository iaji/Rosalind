def readIn():
    with open('rosalind_hamm.txt', 'r' ) as f:
        DNA = f.readlines()
    return DNA

def compDNA(DNA):
    DNAArr = []
    for line in DNA:
        for char in line:
            if char != '\n':
                DNAArr.append(char)
    return DNAArr



def main():
    CompareArr = []
    DNA = readIn()
    Hdist = 0
    y = 0
    for x in range(len(DNA)):
        CompareArr.append(compDNA(DNA[x]))

    for x in range(len(CompareArr[y])):
        if CompareArr[y][x] != CompareArr[y+1][x]:
            Hdist += 1
    return Hdist

ans = main()
print ans
