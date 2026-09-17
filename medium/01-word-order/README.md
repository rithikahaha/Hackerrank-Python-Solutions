# 1. Word Order

[HackerRank link](https://www.hackerrank.com/challenges/word-order/problem)

## What it's asking
Given `n` words (with repeats), print two lines:
1. How many **distinct** words there are.
2. How many times each distinct word appeared, in the order each one was
   **first** seen.

## Steps
1. Go through each word, keeping a running count for each distinct one, and
   remembering the order new words first appear in.
2. Print how many distinct words there are.
3. Print each one's count, in first-appearance order.

## Code
```python
from collections import OrderedDict

n = int(input())
words = OrderedDict()

for _ in range(n):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(*words.values())
```

## Walkthrough
- This uses the same pattern as problem 52 in the Easy section
  (`OrderedDict()`), just measuring counts instead of prices.
- `words.get(word, 0)` fetches the running count for a word, defaulting to
  `0` the first time it's seen, then we add `1` for this occurrence.
- `OrderedDict` remembers the order keys were **first** inserted, so a word
  seen for the first time on line 3 stays in "position 3" in the ordering,
  no matter how many more times it shows up later.
- `len(words)` counts how many distinct words there are — the number of
  keys in the dictionary.
- `print(*words.values())` unpacks all the counts, printing them
  space-separated, in the same first-appearance order the words were
  originally added.
