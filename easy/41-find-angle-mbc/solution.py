import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))
print(f"{round(angle)}°")
