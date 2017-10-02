bcd = input().upper()
v = [1,0,0]
for x in bcd:
    if x == "B":
        v[1],v[0] = v[0],v[1]
        print(v)
    elif x == "C":
        v[1],v[2] = v[2],v[1]
        print(v)
    elif x == "D":
        v[2],v[0] = v[0],v[2]
        print(v)
if v == [1,0,0]:
    print("1")
elif v == [0,1,0]:
    print("2")
elif v == [0,0,1]:
    print("3")


