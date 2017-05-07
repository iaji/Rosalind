
def fib_rabbits(n,k):
    """ Reads in file for n as in number of months and k as in number of babies per split. """
    rabbits = [0,1]
    for i in xrange(n-1):
        rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2]

    return rabbits[n % 2]

with open('rosalind_fib.txt', 'r') as inputs:
    n, k = map(int, inputs.read().strip().split())


print fib_rabbits(n,k)
