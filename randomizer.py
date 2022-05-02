import sys

vals = []
for i in range(38):
    vals.append(0)

def middle_squares(seed, x):
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
        print(seed % 38)
        vals[seed % 38] += 1

middle_squares(sys.argv[1], 1000)

print(vals)