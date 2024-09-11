def suffixsort(s, q):    
    
    sorted_indices = sorted(range(len(s)), key=lambda i: s[i:])
    
    for k in q:
        yield sorted_indices[k]
    
while True:
    try:
        
        s = input().strip()
        q = list(map(int, input().strip().split()))[1:]
        print(" ".join(list(map(str, suffixsort(s, q)))))
    
    except EOFError:
        break
