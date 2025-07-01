with open("Input/numbers.txt") as f1:
    a = f1.read().split()

result1 = list(filter(lambda x: len(x) == 1, a))
result2 = list(filter(lambda x: len(x) == 2, a))
result3 = list(filter(lambda x: len(x) == 3, a))
# 3 xonaligacha xisoblaydi 

with open("Output/output09.txt", "w") as f2:  
    f2.write(str(f"1 xonali sonlar: {len(result1)} ta, "))
    f2.write(str(f"2 xonali sonlar: {len(result2)} ta, "))
    f2.write(str(f"3 xonali sonlar: {len(result3)} ta, ")) 
# kod tushunarli bo'lishi uchun 3 qatar qildm

