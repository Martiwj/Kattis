def abc(number, letter):
    a = min(number)
    c = max(number)
    b = None
    for n in number:
        if n > a and n < c:
            b = n

    dict = {"A": a, "B": b, "C": c}
    outarr = []
    for i in letter:
        if i in dict:
            outarr.append(dict[i])

    print(outarr[0], outarr[1], outarr[2])


number = list(map(int, input().split()))
letters = input()

abc(number, letters)
