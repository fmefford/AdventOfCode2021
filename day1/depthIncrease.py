f = open("C:\\Users\\finnm\\Desktop\\AdventOfCode\\day1\\input.txt", "r")
#last = int(f.readline())
answer = 0
"""
for line in f:
    curr = int(line)
    if curr > last:
        answer += 1
    last = curr
"""

data = f.read().splitlines()
for i in range(3, len(data)):
    if int(data[i]) > int(data[i - 3]):
        answer += 1
print(answer)

