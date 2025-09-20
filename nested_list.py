# result -> Berry Harry

# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

score_list = set()
name_list = []
students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.add(score)
    students.append([score, name])

# print(score_list)
# print(students)
score_list = sorted(score_list)
# print(score_list[1])
second_last = score_list[1]


for i in students:
    if i[0] == second_last:
        name_list.append(i[1])


name_list.sort()
for i in name_list: print(i)





