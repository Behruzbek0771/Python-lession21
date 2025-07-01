f1 = open("Input/numbers.txt")
nums = f1.read().split()

max = max(map(int,nums))

f2 = open("Output/output03.txt",'w')

f2.writelines(f"max: {max}")