# 57. Zipped!

[HackerRank link](https://www.hackerrank.com/challenges/zipped-2/problem)

## What it's asking
You're given `N` (number of students) and `X` (number of subjects), then
`X` lines — each one holding all `N` students' marks for that subject.
Print each student's **average** mark across all `X` subjects, one per
line.

## Steps
1. Read each subject's line of marks, and keep all `X` lists together.
2. Regroup that data **by student** instead of by subject — you need each
   student's marks from every subject gathered together.
3. Average each student's group of marks and print it.

## Code
```python
N, X = map(int, input().split())

subject_marks = []
for _ in range(X):
    subject_marks.append(list(map(float, input().split())))

for student_marks in zip(*subject_marks):
    print(sum(student_marks) / X)
```

## Walkthrough
- After the loop, `subject_marks` is a list of `X` lists — one per subject,
  each containing that subject's mark for all `N` students, in student
  order.
- `zip(a, b, c)` pairs up items from multiple sequences **by position** —
  the first items from each become one group, the second items become the
  next group, and so on.
- `zip(*subject_marks)` uses `*` to unpack the list of subject-lists into
  separate arguments for `zip`. That regroups the data from "by subject" to
  "by student": the first result is every subject's mark for student 1, the
  second result is every subject's mark for student 2, and so on.
- `sum(student_marks) / X` averages one student's group of marks across all
  `X` subjects.
