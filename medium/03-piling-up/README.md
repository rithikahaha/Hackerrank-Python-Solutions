# 3. Piling Up!

[HackerRank link](https://www.hackerrank.com/challenges/piling-up/problem)

## What it's asking
You have a row of cubes with given side lengths. You can only pick cubes
from the **left or right end** of the row (never the middle), and stack
them vertically — but each cube you place must be **no wider** than the one
already beneath it. Figure out whether it's possible to stack every cube in
the row this way. Print `Yes` or `No` for each test case.

## Steps
1. Repeatedly look at both ends of the remaining row.
2. Always take whichever end has the **bigger** cube — since the biggest
   cube left in the row has to be placed *now* if it's ever going to have
   anything smaller stacked on top of it.
3. If that cube is bigger than the last one you placed, stacking is
   impossible — stop and report failure.
4. If you get through every cube this way, it's possible.

## Code
```python
from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')
    valid = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > last:
            valid = False
            break
        last = current

    print("Yes" if valid else "No")
```

## Walkthrough
- A **deque** is the right tool here because we need fast access to *both*
  ends of the row — `cubes[0]` peeks the left end, `cubes[-1]` peeks the
  right end, and `.popleft()` / `.pop()` remove from whichever side we
  choose.
- The core idea: at every step, greedily take the **larger** of the two
  available ends. This works because the biggest cube still in the row
  can *only* go at the very bottom of what's left to build — if you leave it
  in the row and take the smaller end instead, you'll be forced to place
  that big cube on top of something smaller later, which breaks the rule.
- `last` tracks the size of the most recently placed cube (starting at
  infinity, since nothing has been placed yet, so anything is allowed
  first). Every new cube we take must be `<= last`, or the stack is
  impossible — we set `valid = False` and stop checking further as soon as
  that happens.
- If every cube gets placed without ever exceeding the one before it, the
  whole row was stackable, and we print `"Yes"`.
