def adding(a, b, c):

    temp = a+b
    if temp == c:
        return "correct!"
    return "wrong!"


inp = input().split()

a = int(inp[0])
b = int(inp[1])
c = int(inp[2])

print(adding(a, b, c))