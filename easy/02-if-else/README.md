# 02. Python If-Else

[HackerRank link](https://www.hackerrank.com/challenges/py-if-else/problem)

## What it's asking
You're given a number `n`. Print `Weird` or `Not Weird` based on these rules:
- If `n` is odd → `Weird`
- If `n` is even and between 2 and 5 (inclusive) → `Not Weird`
- If `n` is even and between 6 and 20 (inclusive) → `Weird`
- If `n` is even and greater than 20 → `Not Weird`

## Steps
1. Read `n` and convert it to a number (input always comes in as text).
2. Check if `n` is odd first — that's the easiest case, and it's always `Weird`
   no matter what.
3. If it's not odd (so it's even), check which range it falls into, top to
   bottom, and print accordingly.

## Code
```python
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
```

## Walkthrough
- `int(input().strip())` reads the input as text, removes any extra spaces
  with `.strip()`, then converts it to a whole number with `int()`.
- `n % 2` gives you the remainder when `n` is divided by 2. If that remainder
  isn't `0`, the number is odd.
- `elif` means "otherwise, check this next condition" — Python only checks it
  if the one above was false. So by the time we reach `2 <= n <= 5`, we
  already know `n` is even.
- `2 <= n <= 5` is a shortcut for "is n between 2 and 5, including both ends?"
  You could also write it as `n >= 2 and n <= 5`, but this version reads more
  naturally.
- `else` catches everything left over — in this case, even numbers above 20.
