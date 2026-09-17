# 20. Decorators 2 - Name Directory

[HackerRank link](https://www.hackerrank.com/challenges/decorators-2-name-directory/problem)

## What it's asking
Given `N` people, each with a first name, last name, age, and sex, sort
them by **age** (youngest first), and print each one as `"Mr. First Last"`
or `"Ms. First Last"` — using a decorator to handle the sorting, so the
formatting function only has to deal with one already-sorted person at a
time.

## Steps
1. Write a function that formats **one** person's raw data into a readable
   name — it shouldn't need to know anything about sorting.
2. Separately, write a decorator that sorts the whole list of people by age
   *before* handing them, one at a time, to that formatting function.
3. Attach the decorator with `@`.

## Code
```python
def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for _ in range(int(input()))]
    print(*name_format(people), sep='\n')
```

## Walkthrough
- This uses the same decorator pattern as "Standardize Mobile Number Using
  Decorators" in the Easy section — `person_lister` wraps `name_format`, so
  calling `name_format(people)` actually runs `person_lister`'s inner
  function instead.
- `sorted(people, key=lambda x: int(x[2]))` sorts the raw list of people by
  age — `x[2]` is each person's age column, converted to `int` since ages
  arrive as text and need to sort numerically, not alphabetically.
- `[f(person) for person in sorted(...)]` is a list comprehension that
  applies `f` (the *original* `name_format`, before decoration) to each
  person, **one at a time, in the newly sorted order** — collecting all the
  formatted name strings into a list.
- Because all the sorting happens inside the decorator, `name_format`
  itself stays simple: it only has to know how to turn *one* person's raw
  data into a readable string, with no idea that any sorting happened
  around it at all.
- `("Mr. " if person[3] == "M" else "Ms. ")` picks the right title based on
  the person's sex field, then the rest concatenates that title with their
  first and last name.
- `print(*name_format(people), sep='\n')` unpacks the list of formatted
  names and prints each one on its own line.
