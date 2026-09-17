import re
import email.utils

n = int(input())
for _ in range(n):
    line = input()
    name, address = email.utils.parseaddr(line)
    pattern = r'^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$'
    if re.match(pattern, address):
        print(email.utils.formataddr((name, address)))
