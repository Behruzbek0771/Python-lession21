with open('input/grades.csv','r') as f1:
   new_list = []
   students = f1.read()
   for student in students:
       if student.isdigit():
           new_list.append(student)


result = sum(map(int,new_list))
overal = result/len(new_list)

with open('output/output20.txt','w') as f2:
    f2.write(str(overal))