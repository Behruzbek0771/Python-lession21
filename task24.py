with open('input/grades.csv', 'r') as f1:
    new_list = []
    lines = f1.readlines()
    
    for line in lines[1:]:
        name, grade = line.strip().split(',')
        new_list.append((name, int(grade)))

grades = [grade for _, grade in new_list]
average = sum(grades) / len(grades)

new_list2 = []
for name, grade in new_list:
    if grade > average:
        new_list2.append((name, grade))

with open('output/output24.txt', 'w') as f2:
    for name, grade in new_list2:
        f2.write(f"{name},{grade}\n")

