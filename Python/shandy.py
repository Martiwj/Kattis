def pour_shandy(beer, lemonade):
    
    if beer == 0 or lemonade == 0:
        return 0
    
    return pour_shandy(beer-1, lemonade-1) + 2
    
beer = int(input())
lemonade = int(input())

print(pour_shandy(beer, lemonade))

