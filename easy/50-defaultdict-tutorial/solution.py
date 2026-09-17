from collections import defaultdict

n, m = map(int, input().split())

word_positions = defaultdict(list)
for i in range(1, n + 1):
    word = input()
    word_positions[word].append(i)

for _ in range(m):
    word = input()
    if word in word_positions:
        print(*word_positions[word])
    else:
        print(-1)
