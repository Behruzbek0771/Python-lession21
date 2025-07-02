with open("Input/students.txt", "r") as f1:
    harf = f1.read().split()

result = list(map(lambda x: len(x),harf))

with open("Output/output15.txt", "w") as f2:
    f2.write(f"Har bir ism {str(result)} ta harfdan iborat")