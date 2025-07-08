with open('input/grades.csv','r') as f1:
    students_grade = f1.read()
   

with open('output/output19.txt','w') as f2:
    f2.write(students_grade)