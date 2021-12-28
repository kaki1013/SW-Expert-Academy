for t in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    print(f"#{t} {A*B if A < 10 and B < 10 else -1}")
