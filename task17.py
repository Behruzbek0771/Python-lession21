with open("Input/students.txt", "r") as f1:
    students = f1.read().split()
a_names = []
a = list(filter(lambda x : x[0]=="A", students))
a_names.append(a)

with open ("Output/output17.txt", "w") as f2:
    f2.write(f"Ismi 'A' harfi bilan boshlanuvchilarni {str(a_names)} alohida ro'yhati ")
