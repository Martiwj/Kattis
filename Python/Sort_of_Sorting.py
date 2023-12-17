def nameSort(liste):
    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if liste[j][:2] > liste[j+1][:2]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

    return liste


navnliste = []
sortert = []

inp = int(input())
while inp != 0:
    for _ in range(inp):
        navn = input()
        navnliste.append(navn)

    sorted_names = nameSort(navnliste)
    for name in sorted_names:
        sortert.append(name)

    sortert.append("")

    navnliste = []
    inp = int(input())


for i in sortert[:-1]:
    print(i)