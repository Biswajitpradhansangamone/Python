f1 = open("int1.txt","r")
start = int(f1.readline())
end = int(f1.readline())
f2 = open("Assignment.txt","w")

for j in range (start, end+1,1):
    
    for i in range(1,11,1):
        line = str(j)+ str (i) + str (j*i)
        print()
        f2.write(line)
        print()

f2.close()
