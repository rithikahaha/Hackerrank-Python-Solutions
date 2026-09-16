# 20. Capitalize!

[HackerRank link](https://www.hackerrank.com/challenges/capitalize/problem)

## What it's asking
Given a full name, capitalize the first letter of **every word** (e.g.
`"chris alan"` → `"Chris Alan"`). The name might have multiple spaces between
words, and those spaces need to stay exactly as they are.

Note: Python's built-in `.capitalize()` method also *lowercases* the rest of
the word (`"mcDONALD".capitalize()` → `"Mcdonald"`), which isn't what we want
here — we only want to touch the first letter and leave the rest alone.

## Steps
1. Split the name into words, keeping track of the spaces between them.
2. For each word, capitalize just its first letter, leaving the rest of the
   word exactly as it was.
3. Join everything back together with single spaces — since the split step
   preserves extra spaces as empty "words," this naturally keeps multi-space
   gaps intact.

## Code
```python
def solve(s):
    return ' '.join(word[:1].upper() + word[1:] for word in s.split(' '))


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
```

## Walkthrough
- `s.split(' ')` splits only on the space character. If there are two spaces
  in a row, this produces an empty string `""` between them — that's what
  lets us rebuild the original spacing exactly.
- `word[:1]` grabs just the first character of `word` (or `""` if the word
  itself is empty — slicing never raises an error even on an empty string).
  `.upper()` capitalizes it.
- `word[1:]` grabs everything *after* the first character, completely
  untouched — this is how we avoid the "lowercases the rest" problem that
  `.capitalize()` has.
- Adding them together, `word[:1].upper() + word[1:]`, gives you the word
  back with only its first letter changed.
- `' '.join(...)` glues all the words — including the empty ones from
  multiple spaces — back together with single spaces, which reconstructs the
  original spacing pattern.
