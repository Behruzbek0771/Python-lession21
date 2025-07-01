f1 = open("Input/numbers.txt")

nums = f1.readlines()

result = filter(
    lambda num: int(num) % 2 == 0,
    nums
)

f2 = open("Output/output04.txt", 'w')
f2.writelines(result) 