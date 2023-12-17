quad1 = int(input())
quad2 = int(input())

if quad1 < 0 and quad2 > 0:
    print(2)

elif quad1 < 0 and quad2 < 0:
    print(3)

elif (quad1 and quad2) > 0:
    print(1)
elif quad1 > 0 and quad2 < 0:
    print(4)
