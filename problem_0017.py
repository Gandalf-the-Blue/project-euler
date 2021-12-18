# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

from num2words import num2words

total_letter_count = 0
for i in range(1,1001):
    reduced = num2words(i).replace(' ','').replace('-','')
    total_letter_count += len(reduced)

answer = total_letter_count
print(answer)

#21124