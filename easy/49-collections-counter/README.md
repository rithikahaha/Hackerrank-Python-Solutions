# 49. collections.Counter()

[HackerRank link](https://www.hackerrank.com/challenges/collections-counter/problem)

## What it's asking
A shoe shop has a certain number of shoes in each size. Customers come in
one at a time, each wanting a specific size at a specific price. If that
size is still in stock, sell it (add the price to your earnings, reduce
stock by one). Print the total earnings after every customer.

## Steps
1. Read the shop's starting stock, and count how many shoes there are of
   each size.
2. For each customer: check if their size is still in stock.
3. If it is, add the price to earnings and reduce that size's stock by one.
   If not, skip them.
4. Print the total earnings.

## Code
```python
from collections import Counter

X = int(input())
shoe_sizes = Counter(map(int, input().split()))

N = int(input())
earnings = 0

for _ in range(N):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        earnings += price
        shoe_sizes[size] -= 1

print(earnings)
```

## Walkthrough
- `Counter(iterable)` builds something like a dictionary that automatically
  counts how many times each value shows up — here, how many shoes of each
  size are in the starting stock.
- It behaves like a normal dictionary (`shoe_sizes[size]` gives you the
  count for that size), but with one convenient difference: looking up a
  size that was **never** in stock returns `0` instead of raising an error.
  That means we can write `if shoe_sizes[size] > 0:` directly, without first
  checking whether that size exists at all.
- Selling a shoe just means: add its price to `earnings`, and subtract one
  from that size's count — `shoe_sizes[size] -= 1` works exactly like it
  would on a regular dictionary.
