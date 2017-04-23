def readIn():
    with open('example.txt', 'r' ) as f:
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
    for x in range(2):
        CompareArr.append(compDNA(DNA[x]))
    for x in range(len(CompareArr[0])):
        if CompareArr[0][x] != CompareArr[1][x]:
            Hdist += 1
    return Hdist

ans = main()
print ans
