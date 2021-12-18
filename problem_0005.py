#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from collections import Counter

def prime_factors(n):
    factors = []
    c = 2
    while n>1:
        while n%c ==0:
            factors.append(c)
            n //= c
        c +=1
        if c*c>n:
            if n>1 :
                factors.append(n)
            break
    c = Counter(factors)
    return c

result = Counter()

for i in range(1,21):
    factors = prime_factors(i)
    result |= factors

answer = 1

for key in result.keys():
    multiplier = (key)**result[key]
    answer = answer*multiplier

print(answer)

#232792560