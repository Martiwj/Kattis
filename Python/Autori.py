def initals(name):
    inital = ""
    for i in name:
        if i.isupper():
            inital += i

    return inital


inp = input()

print(initals(inp))
