def sort(liste):
    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

    print(liste[0], liste[1])


inp = list(map(int, input().split()))
sort(inp)