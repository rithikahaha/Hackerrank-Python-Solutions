# 4. Time Delta

[HackerRank link](https://www.hackerrank.com/challenges/python-time-delta/problem)

## What it's asking
Given `T` test cases, each with two timestamps (like
`"Sun 10 May 2015 13:54:36 -0700"`), print the number of seconds between
them, as a whole number.

## Steps
1. Parse both timestamps into actual date/time objects that Python
   understands (rather than treating them as plain text).
2. Subtract one from the other.
3. Convert that difference into a number of seconds, and print it (as a
   positive number, no matter which timestamp came first).

## Code
```python
from datetime import datetime


def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    return str(int(abs((dt1 - dt2).total_seconds())))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        t1 = input()
        t2 = input()
        print(time_delta(t1, t2))
```

## Walkthrough
- `datetime.strptime(text, fmt)` parses a date/time string into a real
  `datetime` object, guided by a **format string** describing what each
  part of the text means:
  - `%a` — abbreviated weekday (`Sun`)
  - `%d` — day of month
  - `%b` — abbreviated month name
  - `%Y` — 4-digit year
  - `%H:%M:%S` — hours, minutes, seconds
  - `%z` — the timezone offset (`-0700`)
- Including `%z` matters here: it means Python actually understands each
  timestamp's timezone, so subtracting two timestamps from *different*
  timezones still gives the correct real-world time difference, not just a
  naive text-based comparison.
- `dt1 - dt2` subtracts two `datetime` objects and gives back a `timedelta`
  object — Python's way of representing a *span* of time, rather than a
  specific point in time.
- `.total_seconds()` converts that span into a plain number of seconds (as
  a float), and `int(...)` drops any fractional part. `abs(...)` makes sure
  the result is always positive, regardless of which timestamp was earlier.
