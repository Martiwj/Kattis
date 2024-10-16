n, y = map(int, input().split())


seen = set()
output = []
for i in range(y):
    seen.add(int(input()))
    
for i in range(n):
    if not i in seen:
        output.append(i)
        
    
print("\n".join([str(i) for i in output]))
print(f"Mario got {len(seen)} of the dangerous obstacles.")
    
