T = int(input())
for test in range(1, T+1):
    A, B = map(int, input().split())
    print(f"#{test} {(A + B) % 24}")
