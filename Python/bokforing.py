import sys

input = sys.stdin.read
data = input().splitlines()
m, q = map(int, data[0].split())

restart_value = 0
persons = {}

output = []
for i in range(1, q + 1):
    inp = data[i].split()
    
    if len(inp) == 3:
        persons[inp[1]] = int(inp[2])
    
    elif inp[0] == "PRINT":
        output.append(str(persons.get(inp[1], restart_value)))
    
    elif inp[0] == "RESTART":
        restart_value = int(inp[1])
        persons = {}

sys.stdout.write("\n".join(output) + "\n")