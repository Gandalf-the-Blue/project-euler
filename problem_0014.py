# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def next_collatz_term(n):
    if n%2==0:
        k = n/2
    else:
        k = 3*n +1
    return k

def collatz_chain(n):
    chain = []
    chain.append(n)
    while n!=1:
        n = next_collatz_term(n)
        chain.append(n)
    return len(chain)

max_chain,max_i = 0,1
for i in range(1,1000000):
    chain_length = collatz_chain(i)
    if chain_length>max_chain:
        max_chain = chain_length
        max_i = i

print(max_i)
    
#837799