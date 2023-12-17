def over_snitt_andel(karakterer):
    snitt = sum(karakterer) / len(karakterer)
    over_snitt_teller = sum(1 for karakter in karakterer if karakter > snitt)
    over_snitt_prosent = (over_snitt_teller / len(karakterer)) * 100
    return over_snitt_prosent


antall_tester = int(input())
for _ in range(antall_tester):
    antall_studenter, *karakterer = map(int, input().split())
    prosent = over_snitt_andel(karakterer)
    print("{:.3f}%".format(prosent))