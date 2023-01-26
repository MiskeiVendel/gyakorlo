# 8-királynő probléma (8-queens problem) ///Miskei Vendel///www.miskei.hu

n = 8
from itertools import permutations
szamok = [i + 1 for i in range(n)] 
permut = list(permutations(szamok, n))
for i in permut:
    jo = True
    for e in range(1, n):
        for j in range(0, n - e):
            if abs(i[j] - i[j + e]) == e:
                jo = False
    if jo == True:
        print(i)
           
# ************2023.01.26.************************