import re

with open('Example.data', 'r') as In_Data:
    for line in In_Data:
        if re.findall(('^\<Rosalind_[0-9]+', line):
            print 'hello'
