n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    op = command[0]

    if op == "pop":
        s.pop()
    elif op == "remove":
        s.remove(int(command[1]))
    elif op == "discard":
        s.discard(int(command[1]))

print(sum(s))
