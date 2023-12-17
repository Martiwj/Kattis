def tall(liste):

    r1 = liste[0]
    s = liste[1]
    r2 = (s - r1) + s

    return r2

inp = list(map(int, input().split()))

print(tall(inp))
