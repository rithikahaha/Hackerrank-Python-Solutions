# 11. Finding the Percentage

[HackerRank link](https://www.hackerrank.com/challenges/finding-the-percentage/problem)

## What it's asking
You're given `n` students, each with a name and 3 marks. Then you're given
one `query_name`. Find that student's marks, average them, and print the
average rounded to 2 decimal places.

## Steps
1. Read `n`.
2. For each student, read their name and marks, and store them so you can
   look them up later by name — a **dictionary** is perfect for this.
3. Read `query_name`.
4. Look up that name's marks in the dictionary, average them, and print with
   2 decimal places.

## Code
```python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")
```

## Walkthrough
- `student_marks = {}` creates an empty **dictionary** — a way to store
  values under a name (a "key") so you can fetch them back later with
  `student_marks[name]`, instead of searching through a list.
- `name, *line = input().split()` splits the line into words. The first word
  goes into `name`; the `*line` scoops up *everything else* into a list. This
  is handy because the name always comes first but you don't want to hardcode
  how many marks follow.
- `map(float, line)` converts every mark from text to a number, and
  `list(...)` turns that into an actual list.
- `student_marks[name] = scores` saves that student's marks under their name.
- Once we have `query_name`, `student_marks[query_name]` instantly fetches
  their marks back out.
- `sum(marks) / len(marks)` is just the average: total divided by count.
- `f"{average:.2f}"` is an **f-string** — a way to drop a variable into text.
  The `:.2f` part means "format this as a decimal number with exactly 2
  digits after the point," which also handles the rounding for you.
