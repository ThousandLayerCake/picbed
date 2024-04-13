import sys

data = []
with open("./log.txt", "r") as f:
    while True:
        try:
            content = f.readline().strip().split(" ")
            data.append([int(content[2]), [content[0], content[1]]])
        except:
            break

data.sort()

max_k = 0

left, right = -1, 0

while right < len(data):
    tmp = 0
    while data[right][1][0] == data[right][1][1]:
        
