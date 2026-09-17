# 51. collections.namedtuple()

[HackerRank link](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem)

## What it's asking
You're given `n` students' records. The first line names the columns (e.g.
`ID MARKS NAME CLASS`), and each following line has that student's values in
the same order. Find the average of the `MARKS` column.

## Steps
1. Read the column names.
2. Build a "template" that lets you refer to a row's values by name (like
   `.MARKS`) instead of by position.
3. Read each student's row using that template, and add up their marks.
4. Print the average.

## Code
```python
from collections import namedtuple

n = int(input())
fields = input().split()
Student = namedtuple('Student', fields)

total_marks = 0
for _ in range(n):
    values = input().split()
    student = Student(*values)
    total_marks += int(student.MARKS)

print(total_marks / n)
```

## Walkthrough
- `namedtuple('Student', fields)` builds a new mini "class" called `Student`,
  where each field in `fields` (read from the header line, e.g.
  `['ID', 'MARKS', 'NAME', 'CLASS']`) becomes something you can access by
  name.
- `Student(*values)` creates one `Student` record from a row of values. The
  `*` unpacks the `values` list so each item lines up with the matching
  field name, in order.
- Once you have a `student` object, `student.MARKS` gets you exactly that
  field's value — no need to remember or hardcode "marks is the 2nd
  column." If the column order in the input ever changed, this code would
  still work correctly, since it reads the header to figure out the order
  itself.
- `int(student.MARKS)` converts that value from text to a number so we can
  add it to `total_marks`.
