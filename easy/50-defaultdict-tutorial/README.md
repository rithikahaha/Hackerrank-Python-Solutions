# 50. DefaultDict Tutorial

[HackerRank link](https://www.hackerrank.com/challenges/defaultdict-tutorial/problem)

## What it's asking
You're given `n` words (Group A) and then `m` more words (Group B). For each
word in Group B, print the 1-indexed positions where it appeared in Group A,
space-separated — or `-1` if it never appeared there at all.

## Steps
1. Read Group A's words, and for each one, remember every position (line
   number) it showed up at.
2. For each word in Group B, look up its list of positions from Group A and
   print them — or print `-1` if the word was never in Group A.

## Code
```python
from collections import defaultdict

n, m = map(int, input().split())

word_positions = defaultdict(list)
for i in range(1, n + 1):
    word = input()
    word_positions[word].append(i)

for _ in range(m):
    word = input()
    if word in word_positions:
        print(*word_positions[word])
    else:
        print(-1)
```

## Walkthrough
- With a normal dictionary, doing `word_positions[word].append(i)` on a word
  you haven't seen before would crash — you'd have to check "does this key
  already exist?" and create an empty list yourself before appending to it.
- `defaultdict(list)` removes that hassle: the moment you access a key that
  doesn't exist yet, it automatically creates one with an empty list (`[]`)
  as the starting value. So `word_positions[word].append(i)` just works,
  first time or not, no upfront checking needed.
- For each word in Group A, we record its line number `i` in the list under
  that word — since the same word can appear more than once, each occurrence
  adds another number to its list.
- For Group B, `word in word_positions` checks whether that word ever showed
  up in Group A at all. If it did, `print(*word_positions[word])` unpacks
  its list of positions so they print space-separated; if not, we print
  `-1`.
