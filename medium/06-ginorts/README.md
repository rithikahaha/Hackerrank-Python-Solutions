# 6. ginortS

[HackerRank link](https://www.hackerrank.com/challenges/ginorts/problem)

## What it's asking
Given a string mixing lowercase letters, uppercase letters, and digits,
rearrange all its characters into this exact order:
1. Lowercase letters, alphabetically
2. Uppercase letters, alphabetically
3. Odd digits, ascending
4. Even digits, ascending

(The problem's name, `ginortS`, is actually a hint at the answer if you run
it on the word "Sorting" — see if you can spot why once you read the
walkthrough.)

## Steps
1. Split the string into four separate groups: lowercase letters, uppercase
   letters, odd digits, even digits.
2. Sort each group on its own.
3. Glue the four sorted groups together, in that exact order.

## Code
```python
s = input()

lower = sorted(c for c in s if c.islower())
upper = sorted(c for c in s if c.isupper())
odd_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 1)
even_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 0)

print(''.join(lower + upper + odd_digits + even_digits))
```

## Walkthrough
- Each line builds one group using a generator expression with a filter
  condition — `c for c in s if c.islower()` reads as "every character `c`
  in `s`, but only keep it if `c.islower()` is true." `sorted(...)` then
  arranges that filtered group alphabetically (or numerically, for the
  digit groups).
- Digit characters compare the same way as text or as numbers here (since
  they're single digits), so `sorted(...)` on `'1'`, `'3'`, `'2'` correctly
  gives `['1', '2', '3']` either way — but we still check `int(c) % 2` to
  decide *odd vs even*, since that's a numeric question, not a text one.
- Since these are still lists of individual characters (not one combined
  string yet), `lower + upper + odd_digits + even_digits` just concatenates
  the four lists together, in the required order.
- `''.join(...)` glues that final combined list into one plain string, with
  nothing between the characters.
- Try it on `"Sorting1234"` — you'll get `"ginortS1324"`, which spells out
  the pattern the problem's name is built from: **g**-**i**-**n**-**o**-**r**-**t**
  (lowercase, sorted) then **S** (uppercase) then **1**, **3** (odd digits)
  then **2**, **4** (even digits).
