# 65. XML2 - Find the Maximum Depth

[HackerRank link](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem)

## What it's asking
Same kind of XML tree as the previous problem. This time, find the tree's
**maximum depth** — how many levels deep the most-nested element goes,
counting the root itself as level `0`.

## Steps
1. Parse the XML into a tree.
2. Walk through it, keeping track of how deep each element is (its
   **level**).
3. Every time you reach a new deepest point, remember it.
4. After visiting the whole tree, print the deepest level found.

## Code
```python
import sys
import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    level += 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)


if __name__ == '__main__':
    n = int(input())
    xml_string = "\n".join(input() for _ in range(n))
    tree = etree.ElementTree(etree.fromstring(xml_string))
    depth(tree.getroot(), -1)
    print(maxdepth)
```

## Walkthrough
- `maxdepth` is declared **outside** the function so every recursive call
  can update the same shared value — inside `depth()`, `global maxdepth`
  tells Python "don't create a new local variable, use the one from outside."
- We call `depth(root, -1)` to start. Inside the function, `level += 1`
  immediately makes the root's own level `0` — so the root counts as depth
  `0`, its direct children are depth `1`, their children are depth `2`, and
  so on.
- `maxdepth = max(maxdepth, level)` keeps `maxdepth` updated to whichever is
  bigger: what it already was, or the current element's level. This is a
  common, tidy way to track a running "biggest value seen so far" without
  writing an `if` statement.
- The recursion — `depth()` calling itself on every child — is what lets
  this handle a tree of any depth: each call only has to think about "my own
  level, plus handing the next level down to my children," and the whole
  tree gets covered no matter how deeply it's nested.
