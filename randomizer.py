import sys
import math

vals = []
for i in range(38):
    vals.append(0)

def middle_squares(seed, x):
    seed = abs(int(seed))
    #print(seed)
    n = len(str(seed))
    if n % 2 != 0:
        seed = int(str(seed)[1:])
    n = len(str(seed))
    global vals
    for i in range(x):
        squared = str(seed ** 2).zfill(2 * n)
        a = n // 2
        b = a + n
        seed = int(str(squared)[a:b])
        #print(seed % 38)
        vals[seed % 38] += 1
        #I think we should add a conditional here to scrap bad runs
        if vals[seed % 38] > x/3:
            print("bad run")
            vals = []
            for i in range(38):
                vals.append(0)
            middle_squares(int(sys.argv[1])+1, 100)
            return;

middle_squares(sys.argv[1], 100)

print(vals)
