from collections import Counter

X = int(input())
shoe_sizes = Counter(map(int, input().split()))

N = int(input())
earnings = 0

for _ in range(N):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        earnings += price
        shoe_sizes[size] -= 1

print(earnings)
