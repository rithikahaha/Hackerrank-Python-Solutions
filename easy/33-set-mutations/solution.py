n = int(input())
A = set(map(int, input().split()))
num_ops = int(input())

for _ in range(num_ops):
    op, _ = input().split()
    other_set = set(map(int, input().split()))

    if op == "update":
        A.update(other_set)
    elif op == "intersection_update":
        A.intersection_update(other_set)
    elif op == "difference_update":
        A.difference_update(other_set)
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

print(sum(A))
