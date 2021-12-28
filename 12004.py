s = set()
for i in range(1, 10):
    for j in range(1, 10):
        s.add(i*j)
for t in range(1, int(input()) + 1):
    print(f"#{t} {'Yes' if int(input()) in s else 'No'}")
