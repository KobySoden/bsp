import sys
import math

test = False

#histogram 
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
    
    #variables for storing values
    global vals
    queue = []
    
    for i in range(x):
        squared = str(seed ** 2).zfill(2 * n)
        a = n // 2
        b = a + n
        seed = int(str(squared)[a:b])
        
        vals[seed % 38] += 1
        queue.append(seed % 38)
        #I conditional here to scrap bad runs
        if vals[seed % 38] > x/3:
            #print("bad run")
            vals = []
            for i in range(38):
                vals.append(0)
            return middle_squares(int(sys.argv[1])+1, 100)
            
    return queue

queue = middle_squares(sys.argv[1], 100)

if test == True:
    print(vals)
else:
    print(queue)
