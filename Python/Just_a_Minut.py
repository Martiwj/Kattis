inp = int(input())
total_displayed_minutes = 0
total_actual_seconds = 0

for i in range(inp):
    displayed_minutes, actual_seconds = map(int, input().split())
    total_displayed_minutes += displayed_minutes
    total_actual_seconds += actual_seconds

average_length_of_sl_minute = total_actual_seconds / \
    (total_displayed_minutes * 60)

if average_length_of_sl_minute > 1:
    print("{:.9f}".format(average_length_of_sl_minute))
else:
    print("measurement error")
