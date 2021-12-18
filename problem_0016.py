# What is the sum of the digits of the number 2^1000?

import math

number = int(math.pow(2,1000))
str_number = str(number)
sum =0
for i in range(0,len(str_number)):
    sum += int(str_number[i])

answer = sum
print(answer)

#1366