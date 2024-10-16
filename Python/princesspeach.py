n, y = map(int, input().split())


seen = set()
ignored = []
for _ in range(y):
    seen.add(int(input()))
    
for obstacle in range(n):
    if not obstacle in seen:
        ignored.append(obstacle)
        
    
print("\n".join([str(i) for i in ignored]))
print(f"Mario got {len(seen)} of the dangerous obstacles.")
    
