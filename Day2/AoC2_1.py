"""
Advent of code 2017 day 2 part 1
"""

with open('puzzel1.txt')as f:
    data = [tuple(int(number) for number in numbers.split('\t'))
            for numbers in f.read().split('\n')]
sum = 0
for t in data:
    sum += (max(t) - min(t))
print(sum)
