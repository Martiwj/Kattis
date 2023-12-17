inp = input().strip()

teller = 0

for e in inp:
    if e == "e":
        teller += 1


h = "h"
for i in range(teller*2):
    h += "e"

h += "y"

print(h)
