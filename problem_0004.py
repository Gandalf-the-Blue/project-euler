# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import numpy as np

search_space_p = np.arange(990,99,-11)
search_space_q = np.arange(999,99,-1)
search_space_q = [x for x in search_space_q if x not in search_space_p]

palindromes = []

for p in search_space_p:
    for q in search_space_q:
        check = p*q
        if str(check) == str(check)[::-1]:
            palindromes.append(check)

answer = max(palindromes)
print(answer)

#906609