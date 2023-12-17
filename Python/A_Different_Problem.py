def diff(inp1,inp2):
    if inp1 > inp2:
        return inp1-inp2
    return inp2-inp1


try:
    while True:
        inp1, inp2 = map(int, input().split())
        print(diff(inp1, inp2))
except EOFError:
    pass