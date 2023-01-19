f1 = open("int1.txt","r")
start = int(f1.readline())
end = int(f1.readline())
f2 = open("out1.txt","w")
f2.write("JGHMA")
for j in range(start,end+1,1):
    for i in range(1,11,1):
        print(j,i,j*i)
    print()
f2.close()
