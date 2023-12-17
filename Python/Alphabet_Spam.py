
def spam(stringInn):
    maks = len(stringInn)
    white = 0
    lowercase = 0
    uppercase = 0
    tegn = 0

    for i in stringInn:
        if i == "_":
            white += 1

        elif i.isupper():
            uppercase += 1

        elif i.islower():
            lowercase += 1

        else:
            tegn += 1

    print((white+maks)/maks-1)
    print((lowercase+maks)/maks-1)
    print((uppercase+maks)/maks-1)
    print((tegn+maks)/maks-1)


inp = input()

spam(inp)