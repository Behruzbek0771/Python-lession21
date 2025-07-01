with open("Input/numbers.txt") as f1:
    odd_numbers = f1.read().split()

result =filter(lambda x: int(x)% 2 == 1,odd_numbers)

with open("Output/output06.txt", "w") as f2:
    f2.write("toq sonlar " + ",".join(result))