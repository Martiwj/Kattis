def evenOdd(number):
    if number % 2 == 1:
        print(number, "is odd")
    else:
        print(number, "is even")


amount = int(input())
teller = 0

while teller < amount:
    teller += 1
    ninp = int(input())
    evenOdd(ninp)
