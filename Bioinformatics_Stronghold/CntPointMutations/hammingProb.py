def readIn():
    """ Parses input file into array of lines """
    with open('rosalind_hamm.txt', 'r' ) as f:
        DNA = f.readlines()
        # print DNA
    return DNA

def compDNA(DNA):
    """ Takes in array of lines and splits the lines to characters if the character is not a newline """
    DNAArr = []
    for line in DNA:
        for char in line:
            if char != '\n':
                DNAArr.append(char)
    # print DNAArr
    return DNAArr



def main():
    """ Calls compDNA to append the array of characters to a new Array CompareArr for comparing the same element of two arrays """
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
