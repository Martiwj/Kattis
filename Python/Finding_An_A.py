imp = input()
indeks = next((i for i, char in enumerate(imp) if char == 'a'),None)
liste = imp[indeks:] if indeks is not None else imp

print(liste)