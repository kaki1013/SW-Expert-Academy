import sys

for t in range(1, int(sys.stdin.readline().rstrip()) + 1):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    right = B - A
    stick_length = right * (right + 1) // 2
    ans = stick_length - B
    print(f"#{t} {ans}")
