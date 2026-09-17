# 5. Athlete Sort

[HackerRank link](https://www.hackerrank.com/challenges/python-sort-sort/problem)

## What it's asking
Given a grid of `N` rows and `M` columns of numbers, and a column index `K`,
sort all the rows by the value in column `K` (smallest to largest), and
print the sorted grid.

## Steps
1. Read all the rows.
2. Sort the rows, using each row's value in column `K` as the sort key —
   compared as actual numbers, not text.
3. Print the sorted rows.

## Code
```python
n, m = map(int, input().split())
rows = [input().split() for _ in range(n)]
k = int(input())

rows.sort(key=lambda row: int(row[k]))

for row in rows:
    print(*row)
```

## Walkthrough
- `rows = [input().split() for _ in range(n)]` reads each row as a list of
  text values.
- `.sort(key=...)` sorts a list **in place**, using whatever the `key`
  function returns for each item to decide the order. Here, the key is
  `int(row[k])` — the row's `k`-th column, converted to an actual number.
- Converting to `int` matters: sorting as plain **text** would put `"10"`
  before `"9"` (since `"1"` comes before `"9"` character by character),
  which isn't the numeric order we want.
- Python's sort is **stable** — rows that tie on the sort key keep their
  original relative order from the input. That's a real guarantee, not an
  accident, and it matters whenever a problem cares about tie-breaking by
  "whichever came first."
- `print(*row)` unpacks each row's values so they print space-separated,
  matching the original input format.
