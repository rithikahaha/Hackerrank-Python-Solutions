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
