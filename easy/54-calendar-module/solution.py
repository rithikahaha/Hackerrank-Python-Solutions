import calendar

m, d, y = map(int, input().split())

day_index = calendar.weekday(y, m, d)
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(days[day_index])
