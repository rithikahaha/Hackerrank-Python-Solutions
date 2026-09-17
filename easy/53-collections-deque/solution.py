from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    command = input().split()
    op = command[0]

    if op == "append":
        d.append(int(command[1]))
    elif op == "appendleft":
        d.appendleft(int(command[1]))
    elif op == "pop":
        d.pop()
    elif op == "popleft":
        d.popleft()

print(*d)
