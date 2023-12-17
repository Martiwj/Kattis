board = [1, 1, 2, 2, 2, 8]
inp = input().split()
target = []

for i in range(len(inp)):
    diff1 = board[i]
    diff2 = int(inp[i])
    target.append(diff1-diff2)


print(target[0], target[1], target[2], target[3], target[4], target[5])
