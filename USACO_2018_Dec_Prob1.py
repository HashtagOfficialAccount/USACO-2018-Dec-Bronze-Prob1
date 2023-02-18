x = open("mixmilk.in","r")
l1 = [int(i) for i in x.readline().strip().split()]
l2 = [int(i) for i in x.readline().strip().split()]
l3 = [int(i) for i in x.readline().strip().split()]
x.close()
pos1 = True
pos2 = False
pos3 = False
for i in range(100):
    if pos1 == True:
        if l1[1] + l2[1] <= l2[0]:
            l2[1] = l1[1] + l2[1]
            l1[1] = 0
        else:
            l1[1] = (l1[1] + l2[1]) - l2[0]
            l2[1] = l2[0]
        pos1 = False
        pos2 = True
    elif pos2 == True:
        if l2[1] + l3[1] <= l3[0]:
            l3[1] = l2[1] + l3[1]
            l2[1] = 0
        else:
            l2[1] = (l2[1] + l3[1]) - l3[0]
            l3[1] = l3[0]
        pos2 = False
        pos3 = True
    else:
        if l3[1] + l1[1] <= l1[0]:
            l1[1] = l3[1] + l1[1]
            l3[1] = 0
        else:
            l3[1] = (l3[1] + l1[1]) - l1[0]
            l1[1] = l1[0]
        pos3 = False
        pos1 = True
x = open("mixmilk.out","w")
x.write(str(l1[1])+"\n")
x.write(str(l2[1])+"\n")
x.write(str(l3[1])+"\n")
x.close()
