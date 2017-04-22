
def fib_rabbits(n,k):
    rabbits = [0,1]
    for i in xrange(n-1):
        rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2]

    return rabbits[n % 2]

with open('rosalind_fib.txt') as inputs:
    n, k = map(int, inputs.read().strip().split())
    print n, k
