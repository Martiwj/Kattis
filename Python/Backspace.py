def backspace(inp):
    ny = []

    for char in inp:
        if char == "<":
            if ny:
                ny.pop()
        else:
            ny.append(char)

    return "".join(ny)


inp = input()

print(backspace(inp))
