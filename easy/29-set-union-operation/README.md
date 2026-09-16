# 29. Set .union() Operation

[HackerRank link](https://www.hackerrank.com/challenges/py-set-union/problem)

## What it's asking
You're given the roll numbers of students subscribed to an English
newspaper, and separately, a French newspaper. Print how many students
subscribe to **at least one** of the two.

## Steps
1. Read both lists of roll numbers into sets.
2. Combine them into one set — since sets never hold duplicates, a student
   in both lists only gets counted once.
3. Print how many roll numbers are in that combined set.

## Code
```python
n = int(input())
english = set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))

print(len(english.union(french)))
```

## Walkthrough
- `english.union(french)` merges both sets into one, containing every roll
  number that appears in *either* set. Since it's still a set, any roll
  number that happened to be in both lists only appears once in the result.
- "At least one" is exactly what a union gives you — anyone in `english`,
  `french`, or both, all counted a single time.
- `len(...)` then counts how many students that combined set contains.
