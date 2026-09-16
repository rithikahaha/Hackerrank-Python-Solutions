# 18. Find a String

[HackerRank link](https://www.hackerrank.com/challenges/find-a-string/problem)

## What it's asking
Given a string and a smaller substring, count how many times the substring
appears — **including overlapping matches**. For example, `"CDC"` appears
twice in `"ABCDCDC"`, at positions 2 and 4, and those two matches overlap
(they share the middle `C`).

This overlap rule is exactly why you can't just use Python's built-in
`.count()` method — it skips overlapping matches.

## Steps
1. Go through every possible starting position in the string.
2. At each position, grab a chunk the same length as the substring you're
   searching for.
3. Compare that chunk to the substring. If it matches, count it.
4. Move to the very next position (not past the whole match) — this is what
   makes overlapping matches get counted.

## Code
```python
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
```

## Walkthrough
- `string[i:i + len(sub_string)]` is **slicing** — it grabs a piece of the
  string starting at index `i`, with the same length as `sub_string`. So if
  `sub_string` is `"CDC"` (length 3) and `i` is `2`, this grabs
  `string[2:5]`.
- `range(len(string) - len(sub_string) + 1)` figures out the last valid
  starting position — you stop once there isn't enough room left in `string`
  for a full-length match.
- Because we check `i`, then `i + 1`, then `i + 2`, and so on — one position
  at a time — a match starting at `i` doesn't stop us from also checking
  `i + 1`, which is exactly how overlapping matches get counted correctly.
