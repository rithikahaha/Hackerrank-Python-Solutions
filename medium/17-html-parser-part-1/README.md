# 17. HTML Parser - Part 1

[HackerRank link](https://www.hackerrank.com/challenges/html-parser-part-1/problem)

## What it's asking
Given a block of HTML, print every tag found, along with its attributes —
distinguishing between opening tags (`<div>`), closing tags (`</div>`), and
self-closing tags (`<br/>`).

## Steps
1. Use Python's built-in HTML parsing tool, which already knows how to walk
   through HTML text and recognize tags.
2. Tell it what to *do* each time it finds an opening tag, a closing tag, or
   a self-closing tag.
3. Feed it the HTML text and let it do the work.

## Code
```python
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name, value in attrs:
            print("->", name, ">", value)


n = int(input())
html_code = "\n".join(input() for _ in range(n))

parser = MyHTMLParser()
parser.feed(html_code)
parser.close()
```

## Walkthrough
- `HTMLParser` is a built-in class that already knows how to scan through
  HTML text and recognize its structure — you don't write any parsing logic
  yourself. Instead, you create your **own** class that inherits from it
  (`class MyHTMLParser(HTMLParser):`), and override specific methods to
  define what should happen at each kind of event it finds.
- `handle_starttag(self, tag, attrs)` gets called automatically every time
  the parser finds an opening tag, like `<div class="box">`. `tag` is the
  tag's name (`"div"`); `attrs` is a list of `(name, value)` pairs for each
  attribute — looping through it prints each one.
- `handle_endtag(self, tag)` gets called for closing tags, like `</div>`.
- `handle_startendtag(self, tag, attrs)` gets called for **self-closing**
  tags, like `<br/>` — tags that open and close in one piece, with no
  separate closing tag.
- `.feed(html_code)` hands the full HTML text to the parser, which reads
  through it and calls whichever of the methods above matches each piece it
  finds — you never call these methods yourself; the parser calls them for
  you as it works through the text.
