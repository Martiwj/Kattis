list = [True, False, False]


def shuffel(string):
    if string == "C":
        (list[0], list[2]) = (list[2], list[0])

    elif string == "B":
        (list[1], list[2]) = (list[2], list[1])

    elif string == "A":
        (list[0], list[1]) = (list[1], list[0])


inp = input()

for i in inp:
    shuffel(i)

indeks = 0
for i in list:
    indeks += 1
    if i:
        print(indeks)

