def cold(weather):
    negative = 0

    for temp in weather:
        if temp < 0:
            negative += 1

    return negative


n = int(input())
inp = list(map(int, input().split()))

print(cold(inp))
