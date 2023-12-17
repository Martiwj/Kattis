def binaryS():
    low = 1
    max = 1000
    liv = 10
    while low <= max and liv > 0:

        middel = (low + max) // 2
        print(middel)
        inp = input().lower()

        if inp == "correct":
            return

        elif inp == "lower":
            max = middel - 1
            liv -= 1

        elif inp == "higher":
            low = middel + 1
            liv -= 1


binaryS()
