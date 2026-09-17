N, X = map(int, input().split())

subject_marks = []
for _ in range(X):
    subject_marks.append(list(map(float, input().split())))

for student_marks in zip(*subject_marks):
    print(sum(student_marks) / X)
