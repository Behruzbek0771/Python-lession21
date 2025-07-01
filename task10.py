with open("Input/numbers.txt","r") as file:
    numbers = file.read().split()
    result = sorted(map(int,numbers),key = lambda number: number)

with open("Output/output10.txt",'w') as f2:
    f2.write(str(result))