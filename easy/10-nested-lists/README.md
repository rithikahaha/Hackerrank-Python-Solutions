# 10. Nested Lists

[HackerRank link](https://www.hackerrank.com/challenges/nested-list/problem)

## What it's asking
You're given a list of students, each with a name and a grade. Find the
students with the **second-lowest** grade, and print their names in
alphabetical order (one per line).

## Steps
1. Read each student's name and grade, and store them together as a pair.
2. Collect all the *unique* grades and sort them from lowest to highest.
3. The second-lowest grade is the second one in that sorted list.
4. Go back through the students and find everyone whose grade matches that
   value.
5. Sort those names alphabetically and print them.

## Code
```python
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    unique_scores = sorted(set(score for name, score in students))
    second_lowest = unique_scores[1]

    second_lowest_names = sorted(
        name for name, score in students if score == second_lowest
    )

    for name in second_lowest_names:
        print(name)
```

## Walkthrough
- `for _ in range(int(input())):` repeats a fixed number of times — the
  underscore `_` just means "I'm not going to use this loop variable, I only
  care about repeating the right number of times."
- Each loop reads one name and one score, then stores them together as a
  small list `[name, score]`, appended onto `students`.
- `set(score for name, score in students)` pulls out just the scores (ignoring
  names) and removes duplicates, same idea as in the previous problem.
- `sorted(...)` gives us those unique scores lowest to highest, so
  `unique_scores[1]` (the second item — remember indexing starts at `0`) is
  the second-lowest grade.
- The last step filters `students` down to only the ones matching that grade,
  keeps just their names, and sorts those names alphabetically before
  printing each one on its own line.
