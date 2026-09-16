K = int(input())
rooms = list(map(int, input().split()))

captain_room = (sum(set(rooms)) * K - sum(rooms)) // (K - 1)
print(captain_room)
