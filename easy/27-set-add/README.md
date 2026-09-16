# 27. Set .add()

[HackerRank link](https://www.hackerrank.com/challenges/py-set-add/problem)

## What it's asking
You're given `n` country names, possibly with repeats. Print how many
**distinct** countries there are.

## Steps
1. Start with an empty set.
2. Add each country name to it, one at a time.
3. Since a set can't hold duplicates, its final size is the count of unique
   names — print that.

## Code
```python
if __name__ == '__main__':
    n = int(input())
    countries = set()
    for _ in range(n):
        countries.add(input())
    print(len(countries))
```

## Walkthrough
- `set()` with nothing inside creates an empty set to build up from.
- `.add(value)` inserts one item into a set. If that value is already in the
  set, nothing happens — no error, no duplicate, the set just stays the
  same size.
- Because of that behavior, after adding all `n` names (even with repeats),
  `countries` only contains each unique name once.
- `len(countries)` counts how many items are in the set — which is exactly
  the number of distinct countries.
