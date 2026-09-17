import re

T = int(input())
for _ in range(T):
    uid = input()

    valid = True
    if len(uid) != 10:
        valid = False
    elif not uid.isalnum():
        valid = False
    elif len(re.findall(r'[A-Z]', uid)) < 2:
        valid = False
    elif len(re.findall(r'[0-9]', uid)) < 3:
        valid = False
    elif len(set(uid)) != len(uid):
        valid = False

    print("Valid" if valid else "Invalid")
