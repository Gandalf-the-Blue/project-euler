#What is the value of the first triangle number to have over five hundred divisors?

import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

divisors = 0
i=2
while divisors<500:
    triangle_number = i*(i+1)/2
    num_divisors = len(list(divisorGenerator(triangle_number)))
    if num_divisors>divisors:
        divisors = num_divisors
    i+=1

answer = triangle_number
print(answer)

#76576500