# 53. collections.deque()

[HackerRank link](https://www.hackerrank.com/challenges/py-collections-deque/problem)

## What it's asking
You're given `n` commands — `append x`, `appendleft x`, `pop`, or
`popleft` — to run one after another on an initially empty deque. After all
commands run, print the final contents, space-separated.

## Steps
1. Start with an empty deque.
2. For each command, figure out which operation it is and run it.
3. Print the final deque.

## Code
```python
from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    command = input().split()
    op = command[0]

    if op == "append":
        d.append(int(command[1]))
    elif op == "appendleft":
        d.appendleft(int(command[1]))
    elif op == "pop":
        d.pop()
    elif op == "popleft":
        d.popleft()

print(*d)
```

## Walkthrough
- A **deque** ("double-ended queue") is like a list, but built specifically
  to add and remove items from **both ends** quickly — a regular list is
  slow at removing/inserting from the front once it gets large, while a
  deque handles that just as fast as the back.
- `.append(x)` and `.pop()` work on the **right** end — same as a list.
- `.appendleft(x)` and `.popleft()` work on the **left** end — this is the
  functionality a plain list doesn't give you directly.
- `command[0]` is always the operation name; `command[1]` (when there is
  one) is the value to add — `pop` and `popleft` don't take an argument, so
  we don't try to read one for those.
- `print(*d)` unpacks the deque's contents so they print space-separated on
  one line.
