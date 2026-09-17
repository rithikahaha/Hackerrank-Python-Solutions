from collections import namedtuple

n = int(input())
fields = input().split()
Student = namedtuple('Student', fields)

total_marks = 0
for _ in range(n):
    values = input().split()
    student = Student(*values)
    total_marks += int(student.MARKS)

print(total_marks / n)
