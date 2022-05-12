import sys

numbers = []
for i in range(1,len(sys.argv)):
    #print(i)
    #print(sys.argv[i])
    val = sys.argv[i]
    val = val.replace(",", "")
    val = val.replace("[", "")
    val = val.replace("]", "")
    numbers.append(int(val))

f = open("test.txt", "r")
lines = f.readlines()

position = 0
for i in lines:
    val=i.replace("\n", "");
    numbers[position] += int(val)
    position+=1
f.close()

f = open("test.txt", "w")
for i in numbers:
    f.write(str(i)+"\n")
f.close()

