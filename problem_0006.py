#The sum of the squares of the first ten natural numbers is 385,
# The square of the sum of the first ten natural numbers is 3025,
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_diff(n):
    sum_of_squares = n*(n+1)*(2*n+1)/6
    square_of_sum = n**2 * (n+1)**2 /4
    return square_of_sum - sum_of_squares

answer = sum_square_diff(100)
print(answer)

#25164150