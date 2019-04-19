"""
Advent of code 2017 day 2 
"""
from itertools import combinations

with open('puzzel1.txt')as f:
    data = [tuple(int(number) for number in numbers.split('\t'))
            for numbers in f.read().split('\n')]

# part 1
sum = 0
for t in data:
    sum += (max(t) - min(t))
print(sum)


# part 2

# data = [(5, 9, 2, 8),
# (9, 4, 7, 3),
# (3, 8, 6, 5)]
c=[]
for row in data:
    c.append(tuple(combinations(row,2)))

summe=0
for row in c:
    for elements in row:
        if max(elements) % min(elements) == 0:
            summe += int(max(elements) / min(elements))
print(summe)
