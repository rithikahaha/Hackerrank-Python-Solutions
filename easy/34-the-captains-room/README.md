# 34. The Captain's Room

[HackerRank link](https://www.hackerrank.com/challenges/py-the-captains-room/problem)

## What it's asking
A group of families each has `K` members staying in the same room number, so
every room number shows up exactly `K` times in the list — **except one**,
the captain's room, which shows up only once. Find that one room number.

## Steps
1. Read `K` and the list of room numbers.
2. Get the distinct room numbers (no repeats).
3. Use a bit of math to isolate the one room number that only appeared once
   — see the walkthrough for exactly how.

## Code
```python
K = int(input())
rooms = list(map(int, input().split()))

captain_room = (sum(set(rooms)) * K - sum(rooms)) // (K - 1)
print(captain_room)
```

## Walkthrough
This one leans on a math trick, so let's work through *why* it works rather
than just what it does:

- `sum(set(rooms))` adds up each **distinct** room number once. Multiplying
  that by `K` — `sum(set(rooms)) * K` — gives you what the total would be
  *if every room, including the captain's, had appeared exactly `K` times*.
- `sum(rooms)` is the **actual** total from the real list, where every room
  appears `K` times except the captain's room, which only appears once —
  so it's "missing" `K - 1` copies of the captain's room number compared to
  the imagined total above.
- That means: `sum(set(rooms)) * K - sum(rooms)` equals exactly
  `(K - 1) * captain_room` — the value of the missing copies.
- Dividing by `(K - 1)` isolates `captain_room` on its own.
- `set(rooms)` is what makes this possible in the first place — without it,
  `sum(rooms)` alone can't tell you which room was the odd one out.
