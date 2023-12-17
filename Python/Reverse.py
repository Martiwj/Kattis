def reverse(liste):
    for i in liste[::-1]:
        print(i)


inp = int(input())

teller = 0

liste = []

while teller < inp:
    nyinput = int(input())
    liste.append(nyinput)
    teller += 1

reverse(liste)
