a1 = 2
d = 3
an = 35
n = (an - a1) // d + 1
s = 0
for i in range(a1, an+1, d):
     s += i
print("Сумма элементов прогрессии равна:", s)
