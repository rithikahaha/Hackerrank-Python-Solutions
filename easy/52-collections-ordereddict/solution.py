from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    *name_parts, price = input().split()
    name = " ".join(name_parts)
    items[name] = items.get(name, 0) + int(price)

for name, price in items.items():
    print(name, price)
