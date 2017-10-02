arr = []
for z in range (0,10):
    z = int(input())
    v = z % 42
    arr.append(v)
print(len(set(arr)))
