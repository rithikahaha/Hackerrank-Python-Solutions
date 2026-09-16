# 17. Mutations

[HackerRank link](https://www.hackerrank.com/challenges/python-mutations/problem)

## What it's asking
You're given a string, a position, and a character. Return a new string with
the character at that position replaced.

The catch: in Python, **strings can't be changed in place**. You can't do
`s[2] = "x"` — that raises an error. You have to build a new string instead.

## Steps
1. Turn the string into a list of characters (lists *can* be changed).
2. Change the character at the given position in that list.
3. Join the list back into a single string.

## Code
```python
def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    return "".join(string_list)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```

## Walkthrough
- `list(string)` turns `"abcdef"` into `['a', 'b', 'c', 'd', 'e', 'f']`.
  Unlike a string, a list's individual items *can* be reassigned.
- `string_list[position] = character` replaces just that one character in the
  list.
- `"".join(string_list)` glues the list of characters back into one string,
  with nothing (`""`) between them.
- `i, c = input().split()` reads a line like `"4 z"` and unpacks it directly
  into two variables — `i` (still text, so we convert it with `int()`) and
  `c` (the replacement character).
- The core idea to remember: **strings are immutable** (unchangeable) in
  Python, but you can always convert to a list, make your changes, and
  convert back.
