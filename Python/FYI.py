def numberCheck(ord):
    if ord[:3] == "555":
        return 1
    return 0


inp = input().strip()
print(numberCheck(inp))
