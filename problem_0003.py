#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math
import numpy as np

n = 600851475143

def largest_prime_factor(n):
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
    return factors

answer = largest_prime_factor(n)[-1]
print(answer)

#6857