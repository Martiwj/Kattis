def revers(tall):
    binaer = bin(tall)[2:]
    ny = ""
    for i in binaer[::-1]:
        ny += i

    return int(ny, 2)


inp = int(input())

print(revers(inp))

