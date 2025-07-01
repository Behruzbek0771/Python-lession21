with open("Input/numbers.txt") as f1:
    b = f1.read().split()
result = sum(map(int,b))/len(b)

with open("Output/output05.txt", "w") as f2:
    f2.write(str(f"averge = {result} ga teng"))