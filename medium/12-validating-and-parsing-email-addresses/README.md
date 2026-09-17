# 12. Validating and Parsing Email Addresses

[HackerRank link](https://www.hackerrank.com/challenges/validating-named-email-addresses/problem)

## What it's asking
Given `N` lines like `"DEXTER <dexter@hotmail.com>"`, print only the ones
whose email address is properly formatted — real name and all — and skip
the rest.

## Steps
1. Split each line into its name part and its email part.
2. Check the email part against the rules for a valid address.
3. If it's valid, print the whole `"Name <email>"` line back out.

## Code
```python
import re
import email.utils

n = int(input())
for _ in range(n):
    line = input()
    name, address = email.utils.parseaddr(line)
    pattern = r'^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$'
    if re.match(pattern, address):
        print(email.utils.formataddr((name, address)))
```

## Walkthrough
- `email.utils.parseaddr(line)` is a built-in tool made specifically for
  parsing `"Name <email@domain.com>"` style text — it splits a line like
  that into the name and the email address, handling the surrounding
  punctuation for you instead of you writing your own string-splitting
  logic.
- The regex checks the email address's shape:
  - `^[A-Za-z]` — must **start** with a letter
  - `[A-Za-z0-9._-]*` — followed by any mix of letters, digits, dots,
    underscores, or hyphens
  - `@` — a literal `@` symbol
  - `[A-Za-z]+` — a domain name made only of letters
  - `\.` — a literal dot
  - `[A-Za-z]{1,3}$` — a 1-to-3 letter extension (like `com` or `org`), at
    the very end of the string
- `email.utils.formataddr((name, address))` does the **reverse** of
  `parseaddr` — it reassembles a name and address back into the
  `"Name <email>"` display format. If `name` is empty (the line had no name,
  just a bare email), it correctly formats as just the email with angle
  brackets.
