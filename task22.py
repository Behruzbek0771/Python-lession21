with open('input/grades.csv') as f1:
    grades = f1.read()
    new_list = []
    
    for grade in grades:
        if grade.isdigit():
            new_list.append(grade)

result = new_list.count('5')

with open('output/output22.txt','w') as f2:
    f2.write(str(result))