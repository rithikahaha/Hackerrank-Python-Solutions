from itertools import groupby

S = input()

result = [(len(list(group)), int(key)) for key, group in groupby(S)]
print(*result)
