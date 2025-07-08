with open('input/grades.csv') as f1:
    student_grade = f1.read().strip().split('\n')[1:]

new_list = []
for line in student_grade:
    name, grade = line.split(',')
    if grade == '5':
        new_list.append((name, grade))

with open('output/high_scores.csv', 'w') as f2:
    f2.write('Name,Grade\n')
    for name, grade in new_list:
        f2.write(f"{name},{grade}\n")
