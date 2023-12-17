def main():
    n = int(input())
    friends = []

    for _ in range(n):
        name, like, birthday = input().split()
        like = int(like)
        friends.append((name, like, birthday))

    friends.sort()  
    birthday_memory = {}  

    for name, like, birthday in friends:
        if birthday in birthday_memory:
            if like > birthday_memory[birthday][0]:
                birthday_memory[birthday] = (like, name)
        else:
            birthday_memory[birthday] = (like, name)

    chosen_friends = [name for _, name in birthday_memory.values()]
    chosen_friends.sort()  

    print(len(chosen_friends))
    for name in chosen_friends:
        print(name)

if __name__ == "__main__":
    main()
