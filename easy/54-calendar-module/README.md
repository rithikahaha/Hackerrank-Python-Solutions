# 54. Calendar Module

[HackerRank link](https://www.hackerrank.com/challenges/calendar-module/problem)

## What it's asking
Given a date as `month day year`, find what day of the week it fell on
(e.g. `MONDAY`).

## Steps
1. Read the month, day, and year.
2. Use Python's calendar tools to figure out the day of the week.
3. Print the day name in uppercase.

## Code
```python
import calendar

m, d, y = map(int, input().split())

day_index = calendar.weekday(y, m, d)
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(days[day_index])
```

## Walkthrough
- The `calendar` module already knows how to work out the day of the week
  for any date, following the modern (Gregorian) calendar's rules — there's
  no need to calculate it by hand.
- `calendar.weekday(year, month, day)` returns a number: `0` for Monday,
  `1` for Tuesday, and so on up to `6` for Sunday.
- `days` is a list of day names in that exact same order, starting from
  Monday — so `days[day_index]` looks up the matching name for whatever
  number `weekday()` gave us.
- The names are printed in uppercase because that's the exact format
  HackerRank's checker expects.
