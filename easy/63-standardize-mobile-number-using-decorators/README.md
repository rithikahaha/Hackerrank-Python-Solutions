# 63. Standardize Mobile Number Using Decorators

[HackerRank link](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem)

## What it's asking
You're given a list of phone numbers in inconsistent formats (some with a
country code, some with dashes or spaces). Reformat every one to look like
`+91 xxxxx xxxxx`, then sort and print them — but do the reformatting using
a **decorator**, not by changing the sorting function itself.

## Steps
1. Write the "normal" function that sorts and prints a list of numbers —
   don't worry about formatting inside it at all.
2. Separately, write a decorator that intercepts the list *before* it
   reaches that function, and reformats every number in it.
3. Attach the decorator to the sorting function using `@`.

## Code
```python
def wrapper(f):
    def fun(l):
        f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
```

## Walkthrough
- A **decorator** is a function that wraps another function, letting you add
  behavior *before* or *after* it runs, without changing that function's own
  code. `@wrapper` placed directly above `def sort_phone(l):` means "run
  `sort_phone` through `wrapper` first" — every call to `sort_phone(...)`
  actually calls `wrapper`'s inner function instead.
- `wrapper(f)` takes the original function (`f`, which will be `sort_phone`)
  and returns a brand-new function, `fun`, that does the reformatting and
  *then* calls `f` with the cleaned-up list.
- `c[-10:-5]` and `c[-5:]` use **negative indexing** to grab the last 10
  digits of each number, split into two 5-digit chunks — counting from the
  end like this works no matter whether the original number had an extra
  country code or punctuation stuck on the front.
- Because the formatting logic lives entirely in the decorator, `sort_phone`
  itself stays simple — it only has to sort and print, with no idea that any
  reformatting even happened.
