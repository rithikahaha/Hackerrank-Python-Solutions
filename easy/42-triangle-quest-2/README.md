# 42. Triangle Quest 2

[HackerRank link](https://www.hackerrank.com/challenges/triangle-quest-2/problem)

## What it's asking
Given `n`, print this pattern for rows `1` to `n`:
```
1
121
12321
1234321
```
Each row is a palindrome number that counts up to `i` and back down.

The catch: the official problem asks you to do this using **only math**, no
string tricks — one line of code, using the `for i in range(1, n+1):` loop
already given to you.

## Steps
1. Build a number made of `i` repeated `1`s — called a **repunit** (e.g. for
   `i=3`: `111`).
2. Square that number.
3. Print it.

## Code
```python
for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)
```

## Walkthrough
- `10 ** i - 1` gives a number made entirely of `9`s — for `i=3`, that's
  `999`.
- Dividing by `9` turns those `9`s into `1`s: `999 // 9 = 111`. So
  `(10 ** i - 1) // 9` is a quick way to build a number that's just `i`
  copies of the digit `1`, using pure arithmetic instead of string
  repetition.
- Here's the neat part: squaring a repunit produces exactly the palindrome
  pattern we want. `111 ** 2 = 12321`. `1111 ** 2 = 1234321`. This is a real
  mathematical property of repunits (it holds up to 9 digits, which is all
  this problem needs), not a coincidence — it's the reason this problem
  exists.
- So the whole trick is: build the repunit with arithmetic, square it, print
  it — no loops, no string building required.
