def kombinatorikk(liste):
    sum = 1
    for i in liste:
        sum *= int(i)

    return sum


inp = input().split()

print(kombinatorikk(inp))
