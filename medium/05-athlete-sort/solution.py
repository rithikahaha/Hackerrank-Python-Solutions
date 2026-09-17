n, m = map(int, input().split())
rows = [input().split() for _ in range(n)]
k = int(input())

rows.sort(key=lambda row: int(row[k]))

for row in rows:
    print(*row)
