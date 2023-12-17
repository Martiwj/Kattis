def aah(inp1, inp2):
    if len(inp1) >= len(inp2):
        return "go"
    return "no"


inp1 = input()
inp2 = input()

print(aah(inp1, inp2))
