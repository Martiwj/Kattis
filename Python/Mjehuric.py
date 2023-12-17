inp = input().split()

def bubble(liste):
    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if liste[j] > liste[j+1]:
                (liste[j], liste[j+1]) = (liste[j+1], liste[j])
                output = " ".join(liste)
                print(output)


bubble(inp)
