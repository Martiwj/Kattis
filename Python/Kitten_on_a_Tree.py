if __name__ == "__main__":
    maps = dict()
    katt = int(input())
    inp, *children = map(int, input().split())
    for c in children:
        maps[c] = inp
    root = inp
    while inp != -1:
        try:
            inp, *children = map(int, input().split())
        except ValueError:
            break
        for c in children:
            maps[c] = inp

    path = [katt]
    curr = katt
    while curr != root:
        curr = maps[curr]
        path.append(curr)

    print(" ".join(map(str, (path))))