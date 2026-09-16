# 28. Set .discard(), .remove() & .pop()

[HackerRank link](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem)

## What it's asking
You start with a set of numbers, then get a series of commands —
`pop`, `remove x`, or `discard x` — to run on it, one after another. After
all commands finish, print the sum of whatever numbers are left.

## Steps
1. Read the starting set of numbers.
2. Read how many commands are coming.
3. For each command, figure out which of the three it is and run the
   matching set operation.
4. Once all commands are done, print the sum of the numbers still in the set.

## Code
```python
n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    op = command[0]

    if op == "pop":
        s.pop()
    elif op == "remove":
        s.remove(int(command[1]))
    elif op == "discard":
        s.discard(int(command[1]))

print(sum(s))
```

## Walkthrough
- `.pop()` removes and returns *some* item from the set — since sets have no
  fixed order, you don't get to choose which one, it just takes whatever
  comes out first.
- `.remove(x)` deletes the specific value `x` from the set — but it will
  **raise an error** if `x` isn't actually in the set.
- `.discard(x)` does the same thing as `.remove(x)`, except it stays silent
  and does nothing if `x` isn't there, instead of raising an error. Use
  `.discard()` when you're not sure the value exists and don't want your
  program to crash over it.
- `command = input().split()` splits a line like `"remove 5"` into
  `["remove", "5"]`, so `command[0]` is the operation name and `command[1]`
  (when present) is the value to act on.
