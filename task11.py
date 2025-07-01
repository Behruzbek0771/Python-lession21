f1 = open("Input/students.txt")
name = f1.readlines()

f2 = open("Output/output11.txt", "w")
f2.writelines(name)