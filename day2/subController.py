f = open("C:\\Users\\finnm\\Desktop\\AdventOfCode\\day2\\input.txt", "r")
data = f.read().splitlines()
hori = 0
aim = 0
depth = 0
for datum in data:
    datum = datum.split(" ")
    val = int(datum[1])
    if datum[0] == "forward":
        hori += val
        depth += val*aim
    elif datum[0] == "up":
        aim -= val
    else:
        aim += val
print(depth * hori)
