def spritt(liste,max):
    sum = 0
    for i in liste:
        sum += i
    if sum <= max:
        return "Jebb"
    else:
        return "Neibb"
    

inp = list(map(int, input().split()))
ant = inp[0]
max = inp[1]
rommene = []

for i in range(ant):
    rom = int(input()) 
    rommene.append(rom)

print(spritt(rommene,max))
