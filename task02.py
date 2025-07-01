f1 = open("Input/numbers.txt")
nums = f1.read().split()

sum = 0
for i in nums:
    sum += int(i)
f2 = open("Output/output02.txt",'w')    
f2.write(f"sum : {sum}")