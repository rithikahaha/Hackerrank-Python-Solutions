# 23. String Formatting

[HackerRank link](https://www.hackerrank.com/challenges/python-string-formatting/problem)

## What it's asking
Given a number `n`, print every number from `1` to `n`, showing each one in
decimal, octal, hexadecimal, and binary — all lined up in neat columns, each
right-aligned to the same width.

## Steps
1. Work out the width you need: it's the length of the *widest* value across
   all numbers and all formats. That's always the binary form of `n` itself,
   since binary takes the most digits.
2. For each number from `1` to `n`, work out its decimal, octal, hex, and
   binary text.
3. Right-align each one to that width and print them together on one line.

## Code
```python
def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
```

## Walkthrough
- `bin(i)`, `oct(i)`, and `hex(i)` are built-in functions that convert a
  number into text in a different base. They each add a prefix showing which
  base it is — `"0b"`, `"0o"`, `"0x"` — so we slice it off with `[2:]` since
  we only want the digits.
- `hex(i)[2:].upper()` also uppercases the letters in hex output (like `a` →
  `A`), since HackerRank expects uppercase hex digits.
- `width = len(bin(number)[2:])` measures the length of the binary form of
  the *largest* number in our range (`number` itself) — since binary always
  needs the most digits of any of the four formats, this one measurement is
  enough to size every column correctly.
- `.rjust(width)` right-aligns a piece of text by padding spaces on the
  **left** until it reaches `width` characters — this is what keeps every
  column lined up regardless of how many digits each individual number has.
