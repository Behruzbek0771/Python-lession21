f1 = open("Input/students.txt")
name = f1.readlines()

result = len(name)

f2 = open("Output/output12.txt", "w")
f2.writelines(f" Ro'yhatdagi ismlar soni {str(result)} ta")