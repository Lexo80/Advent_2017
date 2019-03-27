"""
Advent of Code 2017"
day 1 star 1
"""

with open('Puzzle.txt') as f:
    data = f.read()
    captcha=0
    for i in range(len(data)):
        if i is 0:
            if data[i] == data[-1]:
                captcha += int(data[i])
        else:
            if data[i] == data[i-1]:
                captcha += int(data[i])
    print(captcha)        
            
        