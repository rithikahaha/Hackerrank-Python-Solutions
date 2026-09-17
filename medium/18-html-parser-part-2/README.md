# 18. HTML Parser - Part 2

[HackerRank link](https://www.hackerrank.com/challenges/html-parser-part-2/problem)

## What it's asking
Given a block of HTML, find every **comment** (`<!-- like this -->`) and
every piece of actual visible **text content**. Label comments as
single-line or multi-line, and skip printing any text that's just blank
whitespace.

## Steps
1. Use the same `HTMLParser` tool from Part 1, but this time override the
   methods for comments and text data instead of tags.
2. For a comment, check whether it spans multiple lines to decide which
   label to print.
3. For text data, skip it entirely if it's just whitespace; otherwise print
   it.

## Code
```python
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


parser = MyHTMLParser()

n = int(input())
html_code = "\n".join(input() for _ in range(n))
parser.feed(html_code)
```

## Walkthrough
- `handle_comment(self, data)` is called whenever the parser finds an HTML
  comment. `data` holds just the text **inside** the `<!--` and `-->`
  markers, with the markers themselves already stripped off.
- `'\n' in data` checks whether that comment text contains a line break —
  if it does, the comment spans multiple lines in the original source, so
  we label it `"Multi-line Comment"`; otherwise `"Single-line Comment"`.
- `if data.strip():` only prints the comment's actual text if there's
  something there besides whitespace — `.strip()` returns an empty string
  for blank/whitespace-only text, which Python treats as "falsy" (so the
  `if` skips it).
- `handle_data(self, data)` is called for the plain text sitting between
  tags — not the tags themselves, just the visible content. HTML source
  often has stray blank lines and indentation between tags that aren't
  meaningful content, so the same `data.strip()` check filters those out,
  only printing genuinely non-blank text.
