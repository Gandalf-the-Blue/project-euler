import math

n = math.factorial(100)
digits = [int(digit) for digit in str(n)]
answer = sum(digits)
print(answer)

#648