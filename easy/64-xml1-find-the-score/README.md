# 64. XML 1 - Find the Score

[HackerRank link](https://www.hackerrank.com/challenges/xml-1-find-the-score/problem)

## What it's asking
You're given an XML document (a tree of nested elements, where each element
can have its own attributes and its own child elements inside it). Count
the **total number of attributes** across every element in the whole tree.

## Steps
1. Parse the XML text into a tree structure you can walk through.
2. For each element, count its own attributes.
3. Do the same for all of its children, and all of *their* children, and so
   on — then add everything up.

## Code
```python
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(child) for child in node)


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
```

## Walkthrough
- `xml.etree.ElementTree` is Python's built-in tool for parsing XML text
  into an actual tree of elements you can navigate in code, rather than
  treating it as one long block of text.
- Each element has `.attrib` — a dictionary of that element's own attributes
  (like `name="value"` pairs). `len(node.attrib)` counts how many that one
  element has.
- Since an XML tree can nest arbitrarily deep (elements inside elements
  inside elements...), we use **recursion**: `get_attr_number` calls itself
  on each of a node's children. Each call handles one element and trusts
  the recursive calls to correctly handle everything nested inside it —
  this naturally covers a tree of *any* depth, without needing to know how
  deep it goes ahead of time.
- `sum(get_attr_number(child) for child in node)` adds up the attribute
  counts from every child, and we add that to the current node's own count
  (`len(node.attrib)`) to get the running total.
