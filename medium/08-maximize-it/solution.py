from itertools import product

K, M = map(int, input().split())

arrays = []
for _ in range(K):
    parts = list(map(int, input().split()))
    arrays.append(parts[1:])

max_value = 0
for combo in product(*arrays):
    value = sum(x ** 2 for x in combo) % M
    max_value = max(max_value, value)

print(max_value)
