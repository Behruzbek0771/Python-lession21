with open("Input/students.txt", "r") as f1:
    harf = f1.read().split()

result = list(filter(lambda x: len(x) > 5,harf))
print(result)
with open("Output/output16.txt", "w") as f2:
    f2.write(f" Ismi 5 harfdan uzun bo'lgan talabalar{str(result)}")