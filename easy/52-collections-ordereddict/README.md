# 52. collections.OrderedDict()

[HackerRank link](https://www.hackerrank.com/challenges/py-collections-ordereddict/problem)

## What it's asking
You're given `n` lines, each an item name (which might have multiple words)
followed by its price. If the same item name appears more than once, its
prices should be added together. Print each distinct item name with its
total price, in the order each name was **first** seen.

## Steps
1. Go through each line, splitting off the price from the item name.
2. Keep a running total for each item name.
3. Once all lines are read, print each item name and its total, in the order
   the names first appeared.

## Code
```python
from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    *name_parts, price = input().split()
    name = " ".join(name_parts)
    items[name] = items.get(name, 0) + int(price)

for name, price in items.items():
    print(name, price)
```

## Walkthrough
- `*name_parts, price = input().split()` splits the line into words, then
  unpacks them: `price` grabs the **last** word, and `*name_parts` scoops up
  **everything before it** into a list. This handles item names with any
  number of words, since price is always guaranteed to be the final token.
- `" ".join(name_parts)` glues the name's words back into a single string
  with spaces between them.
- `items.get(name, 0)` looks up the running total for this name so far,
  defaulting to `0` the first time we see it — this avoids a crash on a
  name that isn't in the dictionary yet.
- `OrderedDict` works like a regular dictionary, but makes a point of
  remembering the order keys were first added — so when we loop over
  `items.items()` at the end, the names come out in the same order they
  first appeared in the input, which is exactly what the problem wants.
  (Modern Python dictionaries actually preserve insertion order too, but
  `OrderedDict` makes that guarantee explicit — which is the whole point of
  this exercise.)
