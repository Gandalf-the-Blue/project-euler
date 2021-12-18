# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

import math
import numpy as np

def trial_division_wheel_factorization(n):
    is_prime = True
    if n<=3 or n==5:
#first checking if n<=3 as then it is obviously prime
        is_prime = True
    elif n%2==0 or n%3==0 or n%5==0:
#next checking if n is divisible by 2,3 or 5
        is_prime=False
    else:
#using Wheel Factorization such that now, every integer can be represented as 30k+i but for i divisible by 2,3,5 the number will not be prime. This leaves the values of i that may be prime as = 1, 7, 11, 13, 17, 19, 23, 29. We use this fact to reduce the number of checks to make.
        max_check = math.ceil(math.sqrt(n))
        checks = np.array(range(3,max_check+1,2))
        checks = [s for s in checks if s%30==1 or s%30==7 or s%30==11 or s%30==13 or s%30==17 or s%30==19 or s%30==23 or s%30==29]
        checker = [n%i for i in checks]
        if 0 in checker:
            is_prime=False
    return(is_prime)

def nth_prime(n):
    primes=[2]
    i = primes[-1] +1
    while len(primes)<n:
        if trial_division_wheel_factorization(i)==True:
            primes.append(i)
            i+=1
        else:
            i +=1
    return primes

answer = nth_prime(10001)[-1]
print(answer)

#104743