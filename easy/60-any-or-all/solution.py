n = int(input())
nums = input().split()

all_positive = all(int(x) > 0 for x in nums)
any_palindrome = any(x == x[::-1] for x in nums)

print(all_positive and any_palindrome)
