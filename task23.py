from collections import Counter

with open('input/grades.csv','r') as f1:
    grades = f1.read()
    new_list = []
    for grade in grades:
        if grade.isdigit():
            new_list.append(int(grade))

countes = Counter(new_list)

with open('output/output23.txt','w') as f2:
    f2.write(str(countes))