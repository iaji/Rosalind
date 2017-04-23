from Bio import SeqIO

def GetGCPer(sequence):
    G = sequence.count('G')
    C = sequence.count('C')
    GC = G + C
    return 100 * (GC / float(len(sequence)))

def GrabData():
    DNA_Sequences = SeqIO.parse(open('data.txt'),'fasta')
    tup = ()
    GCPercents = []
    for fasta in DNA_Sequences:
        name, sequence = fasta.id, fasta.seq.tostring()
        GCper = GetGCPer(sequence)
        tup = (name, GCper)
        GCPercents.append(tup)
    return GCPercents

def main():
    x = []
    data = GrabData()
    for tup in data:
        x.append(tup[1])
    best = max(x)
    for tup in data:
        if tup[1] == best:
            print tup
main()
