students = []
student_count = int(input())
for _ in range(student_count):
        n = input()
        score = float(input())
        students.append([n, score])
print(students)

ls = sorted(students, key=lambda x: [x[1], x[0]])

if student_count== 2:
    print(ls[0][0])
    print(ls[1][0])
    exit()
else:
    print(ls[1][0])
    print(ls[2][0])

