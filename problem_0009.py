# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagorean_triplet_sum(n):
    for a in range(n//3-1,2,-1):
        b = n*(n-2*a)//(2*(n-a))
        c = n-a-b
        if a*a + b*b == c*c:
            triplet = [a,b,c]
            p = a*b*c
            return(triplet,p)

            break

answer = pythagorean_triplet_sum(1000)

print(answer)

#([200, 375, 425], 31875000)