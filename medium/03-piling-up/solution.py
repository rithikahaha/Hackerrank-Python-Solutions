from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')
    valid = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > last:
            valid = False
            break
        last = current

    print("Yes" if valid else "No")
