s = input()

lower = sorted(c for c in s if c.islower())
upper = sorted(c for c in s if c.isupper())
odd_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 1)
even_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 0)

print(''.join(lower + upper + odd_digits + even_digits))
