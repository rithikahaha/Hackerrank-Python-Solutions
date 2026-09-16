# 12. Lists

[HackerRank link](https://www.hackerrank.com/challenges/python-lists/problem)

## What it's asking
You're given `N` commands, one per line, like `insert 2 5` or `print`. Start
with an empty list and carry out each command as it comes in — `insert`,
`print`, `remove`, `append`, `sort`, `pop`, `reverse`.

## Steps
1. Read `N`.
2. Start with an empty list.
3. For each of the `N` lines, figure out which command it is and what
   arguments (if any) go with it.
4. Run the matching list operation.

## Code
```python
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        op = command[0]
        args = command[1:]

        if op == "insert":
            lst.insert(int(args[0]), int(args[1]))
        elif op == "print":
            print(lst)
        elif op == "remove":
            lst.remove(int(args[0]))
        elif op == "append":
            lst.append(int(args[0]))
        elif op == "sort":
            lst.sort()
        elif op == "pop":
            lst.pop()
        elif op == "reverse":
            lst.reverse()
```

## Walkthrough
- `input().split()` breaks a line like `"insert 2 5"` into
  `["insert", "2", "5"]`.
- `command[0]` is always the command name; `command[1:]` is everything after
  it — the arguments, if there are any. This works whether there are zero,
  one, or two arguments.
- Each `elif` matches one possible command and calls Python's built-in list
  method that does the same thing:
  - `.insert(index, value)` — puts `value` at position `index`
  - `.remove(value)` — deletes the first occurrence of `value`
  - `.append(value)` — adds `value` to the end
  - `.sort()` — sorts the list in place, smallest to largest
  - `.pop()` — removes and discards the last item
  - `.reverse()` — flips the order of the list in place
- Arguments always arrive as text, so anywhere we need a number (like the
  index or value for `insert`), we convert it with `int(...)` first.
