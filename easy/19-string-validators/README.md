# 19. String Validators

[HackerRank link](https://www.hackerrank.com/challenges/string-validators/problem)

## What it's asking
Given a string, print `True` or `False` (one per line) for whether it
contains **at least one** character that is:
1. Alphanumeric (a letter or a digit)
2. A letter
3. A digit
4. Lowercase
5. Uppercase

## Steps
For each of the 5 checks:
1. Look at every character in the string.
2. Ask "does this one match?"
3. If *any* character matches, the answer is `True`; otherwise `False`.

## Code
```python
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
```

## Walkthrough
- `c.isalnum()`, `c.isalpha()`, `c.isdigit()`, `c.islower()`, `c.isupper()`
  are all built-in checks you can run on a single character — each returns
  `True` or `False`.
- `c.isalnum()` on its own means "is `c` *either* a letter or a digit,"
  which is what "alphanumeric" means.
- `(c.isalnum() for c in s)` is a **generator expression** — it looks just
  like a list comprehension (`[c.isalnum() for c in s]`), but instead of
  building the whole list in memory, it checks characters one at a time as
  needed. For this problem either works — a generator is just a bit more
  efficient.
- `any(...)` looks through that sequence of `True`/`False` values and
  returns `True` the moment it finds even one `True`. If none of them are
  `True`, it returns `False`. That's exactly "does at least one character
  match?"
