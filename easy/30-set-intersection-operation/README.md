# 30. Set .intersection() Operation

[HackerRank link](https://www.hackerrank.com/challenges/py-set-intersection-operation/problem)

## What it's asking
Same setup as the previous problem — English and French newspaper
subscribers — but this time print how many students subscribe to **both**.

## Steps
1. Read both lists of roll numbers into sets.
2. Find the roll numbers that appear in both sets.
3. Print how many there are.

## Code
```python
n = int(input())
english = set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))

print(len(english.intersection(french)))
```

## Walkthrough
- `english.intersection(french)` returns only the values present in **both**
  sets — everything they have in common.
- Compare this with the previous problem: `.union()` was "in either one,"
  `.intersection()` is "in both." Same two sets, different question, and
  Python has a dedicated method for each.
- `len(...)` counts how many roll numbers ended up in that overlap.
