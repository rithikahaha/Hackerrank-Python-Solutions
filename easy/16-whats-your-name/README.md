# 16. What's Your Name?

[HackerRank link](https://www.hackerrank.com/challenges/whats-your-name/problem)

## What it's asking
You're given a first name and a last name, each on its own line. Print:
`Hello firstname lastname! You just delved into python.`

## Steps
1. Read the first name.
2. Read the last name.
3. Print the greeting with both names slotted in.

## Code
```python
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
```

## Walkthrough
- `f"Hello {first} {last}! ..."` is an **f-string** — putting `f` right
  before the opening quote lets you drop variables directly into the text by
  wrapping them in `{}`. It's much easier to read than gluing pieces together
  with `+`.
- This problem is mostly practice at defining a function that takes two
  inputs (`first`, `last`) and does something with them, rather than
  returning a value — here it just prints directly instead of returning text.
