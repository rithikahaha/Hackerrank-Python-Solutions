# 08. List Comprehensions

[HackerRank link](https://www.hackerrank.com/challenges/list-comprehensions/problem)

## What it's asking
You're given four numbers: `x`, `y`, `z`, `n`. Find every combination
`[i, j, k]` where:
- `i` is any number from `0` to `x`
- `j` is any number from `0` to `y`
- `k` is any number from `0` to `z`
- and `i + j + k` does **not** equal `n`

Print all those combinations as a list.

## Steps
1. Read `x`, `y`, `z`, `n`.
2. Try every possible `i`, then for each `i` try every possible `j`, then for
   each of those try every possible `k` (three loops, one inside another).
3. Every time `i + j + k` isn't equal to `n`, save `[i, j, k]`.
4. Print all the saved combinations.

## The "long way" first
It helps to write this with plain loops before reaching for the shortcut:

```python
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    result.append([i, j, k])

    print(result)
```

## The shortcut: list comprehensions
Once the logic above makes sense, this is what a **list comprehension** does
— it's the exact same three loops and the same `if` check, just written on
one line:

```python
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i, j, k]
           for i in range(x + 1)
           for j in range(y + 1)
           for k in range(z + 1)
           if i + j + k != n])
```

## Walkthrough
- `range(x + 1)` gives `0, 1, ..., x` — remember `range` stops one short, so
  `+ 1` is needed to actually *include* `x`.
- Three loops nested inside each other means: for every `i`, go through every
  `j`; for every one of those, go through every `k`. That's how you get every
  possible combination of the three.
- A list comprehension reads left to right as: "give me `[i, j, k]`, for each
  `i` in this range, for each `j` in this range, for each `k` in this range,
  but only if this condition is true." It's just a for-loop and an `append`,
  compressed into one line.
- Neither version is "more correct" — the loop version is easier to read
  while you're learning; the comprehension is what you'll see more often
  once you're comfortable, because it's shorter.
