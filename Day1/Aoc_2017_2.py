"""
Advent of code day 1
part 2
"""

sum = 0

with open('Puzzle2.txt') as f:
    data = [int(s) for s in f.read()]

datalength = int(len(data))
nextItem = int(datalength / 2)

for s in range(datalength):
    index = (s + nextItem) % datalength
    if data[s] == data[index]:
        sum += data[s]
print(sum)
