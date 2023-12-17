def problems(probs):
    teller = 0
    for num in range(len(probs)):
        if "-" in probs[num]:
           f = probs[num].split("-")
           rang = (int(f[1]) - int(f[0])) + 1
           teller += rang

        else:
            teller += 1

    return teller


inp = input().split(";")

print(problems(inp))
