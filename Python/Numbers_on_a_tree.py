h = int(input())
path = input().strip()

cur = 1
for c in path:
    cur = cur * 2 + (c == 'R')

print((1 << (h + 1)) - cur)
