f1 = open("Input/students.txt")
name = f1.readlines()

name.reverse()

f2 = open("Output/output14.txt", "w")
f2.writelines(name)