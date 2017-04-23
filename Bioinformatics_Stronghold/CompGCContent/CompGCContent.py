import re
regexp = re.compile(r'Rosalind.')
output = ''
DNAinfo = open('data.txt')
lines = DNAinfo.readlines()
StrandPart = []
FinishedStrand = ''
#StrandCount = 0
for line in lines:
    while not regexp.search(line) and len(line) == 61:
        for char in line:
            MostStrand = ''.join(char)

print MostStrand
