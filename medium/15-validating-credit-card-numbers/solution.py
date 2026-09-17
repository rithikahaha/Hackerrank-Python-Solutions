import re

n = int(input())
for _ in range(n):
    card = input()

    valid = True
    if not re.match(r'^[456]\d{3}(-?\d{4}){3}$', card):
        valid = False
    elif re.search(r'(\d)\1{3,}', card.replace('-', '')):
        valid = False

    print("Valid" if valid else "Invalid")
