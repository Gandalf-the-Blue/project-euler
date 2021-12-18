#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
import numpy as np

multiples_of_3 = np.arange(3,1000,3)
multiples_of_5 = np.arange(5,1000,5)
multiples_of_15 = np.arange(15,1000,15)
answer = np.sum(multiples_of_3) + np.sum(multiples_of_5) - np.sum(multiples_of_15)
print(answer)

#233168