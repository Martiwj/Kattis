def calculate_qaly(periods):
    total_qaly = 0.0
    for period in periods:
        q, y = period
        qaly = q * y
        total_qaly += qaly
    return total_qaly

N = int(input())
periods = []
for _ in range(N):
    q, y = map(float, input().split())
    periods.append((q, y))

result = calculate_qaly(periods)
print(result)