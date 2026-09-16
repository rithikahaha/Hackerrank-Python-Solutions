# 33. Set Mutations

[HackerRank link](https://www.hackerrank.com/challenges/py-set-mutations/problem)

## What it's asking
You have a set `A`. You're then given a series of commands — `update`,
`intersection_update`, `difference_update`, `symmetric_difference_update` —
each paired with another set. Each command should **change `A` itself**
(not just calculate a new set and throw it away). After all commands, print
the sum of what's left in `A`.

## Steps
1. Read set `A`.
2. For each command: read which operation it is, read the other set, then
   apply the matching in-place update to `A`.
3. Print the sum of `A` once every command has run.

## Code
```python
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
```

## Walkthrough
- You've already met `.union()`, `.intersection()`, `.difference()`, and
  `.symmetric_difference()` — each of those **returns a brand-new set** and
  leaves the original sets untouched.
- These four methods do the exact same calculations, but **change the set
  you call them on, in place**, instead of returning something new:
  - `A.update(other)` — same result as `A = A.union(other)`
  - `A.intersection_update(other)` — same as `A = A.intersection(other)`
  - `A.difference_update(other)` — same as `A = A.difference(other)`
  - `A.symmetric_difference_update(other)` — same as
    `A = A.symmetric_difference(other)`
- `op, _ = input().split()` reads a line like `"intersection_update 4"` — the
  operation name goes into `op`, and the number after it (how many values
  are on the *next* line) gets thrown away into `_` since we don't actually
  need it; `input().split()` on the following line reads the actual values.
