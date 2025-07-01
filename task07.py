with open("Input/numbers.txt") as f1:
    Kv = f1.read().split()

result = list(map( lambda x: pow(int(x),2),Kv))

with open("Output/output07.txt" , "w") as f2:
    f2.write(str(f"Kvadratlari: {result}"))
