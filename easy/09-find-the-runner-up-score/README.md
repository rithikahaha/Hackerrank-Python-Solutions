# 09. Find the Runner-Up Score!

[HackerRank link](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)

## What it's asking
You're given a list of scores. Print the **second-highest** score — but if
the highest score appears more than once, it still only counts as one value
(you want the second-highest *unique* score, not just the second entry in
the list).

## Steps
1. Read the list of scores.
2. Remove duplicate scores, since repeats of the top score shouldn't count
   twice.
3. Sort what's left from lowest to highest.
4. The second-highest unique score is the second one from the end.

## Code
```python
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    unique_scores = list(set(arr))
    unique_scores.sort()

    print(unique_scores[-2])
```

## Walkthrough
- `input().split()` breaks the line of scores up wherever there's a space,
  giving you a list of text pieces like `['5', '2', '8']`.
- `map(int, ...)` converts every piece in that list from text to a number, and
  `list(...)` turns the result back into an actual list you can use.
- `set(arr)` removes duplicates — a **set** in Python can only hold each value
  once. Converting the list to a set and back (`list(set(arr))`) is a quick
  way to de-duplicate.
- `.sort()` arranges the numbers from lowest to highest, in place.
- `unique_scores[-2]` uses negative indexing: `-1` is the last item (the
  highest score), so `-2` is the one right before it — the second-highest.
