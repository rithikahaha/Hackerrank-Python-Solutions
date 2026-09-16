# 14. sWAP cASE

[HackerRank link](https://www.hackerrank.com/challenges/swap-case/problem)

## What it's asking
Given a string, flip the case of every letter — uppercase becomes lowercase
and lowercase becomes uppercase. Non-letters (numbers, spaces, punctuation)
stay exactly as they are.

## Steps
1. Go through the string one character at a time.
2. If the character is uppercase, make it lowercase.
3. If it's lowercase, make it uppercase.
4. Otherwise, leave it untouched.
5. Stick all the characters back together into one string.

## The "long way" first
```python
def swap_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```

## The shortcut
Python strings already have a built-in method that does exactly this:

```python
def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```

## Walkthrough
- `char.isupper()` and `char.islower()` check a single character's case and
  return `True` or `False`.
- `char.lower()` / `char.upper()` convert a character (or a whole string) to
  the opposite case.
- We build the answer up one character at a time with `result += ...`, same
  pattern as the "Print Function" problem earlier.
- `.swapcase()` is a built-in string method that does this entire loop for
  you in one call. It's worth writing the manual version first so you
  understand *why* it works — after that, reaching for `.swapcase()` is just
  saving yourself the typing.
