f1 = open("Input/students.txt")
name = f1.readlines()

name.sort()

f2 = open("Output/output13.txt", "w")
f2.writelines(name)