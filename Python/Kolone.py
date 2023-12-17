row1, row2 = map(int, input().split())
ant_row1 = [_ for _ in input()]
ant_row2 = [_ for _ in input()]
T = int(input())

ants = ant_row2[::-1] + ant_row1
meet_point = len(ant_row2)

for _ in range(T):
    i = 0
    while i < len(ants)-1:
        if ants[i] in ant_row2 and ants[i+1] in ant_row1:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i+=2
        else:
            i+= 1

order_after_T_seconds = ants[:meet_point] + ants[meet_point:]

print("".join(order_after_T_seconds[::-1]))
