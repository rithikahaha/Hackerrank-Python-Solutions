A = set(map(int, input().split()))
n = int(input())

is_strict_superset = True
for _ in range(n):
    other = set(map(int, input().split()))
    if not (A.issuperset(other) and len(A) > len(other)):
        is_strict_superset = False

print(is_strict_superset)
