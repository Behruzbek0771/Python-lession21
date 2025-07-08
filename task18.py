with open('input/students.txt','r') as f1:
    
    students = f1.read().split()
    result = map(lambda student:student.lower(),students)
    name = input("enter your name : ").lower()
    
with open('output/output18.txt','w') as f2:
    if name in result:
        f2.write('True')
    else:
        f2.write("False")