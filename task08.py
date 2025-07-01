with open("Input/numbers.txt") as f1:
    a = f1.read().split()
result = list(filter(lambda x: int(x) % 5 == 0, a))

with open("Output/output08.txt", "w") as f2:
    f2.write(str(f"5 ga karrali sonlar {result} dan iborat"))