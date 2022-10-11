import re
allData = []
VD = []
i = 0
j = 0 


with open('data.txt','r') as data:
    while True:
        l = data.readline()
        tempData = re.split(r' ',l)
        if '-' in tempData:
            VD.append(l)
        # allData.append(tempData)
        if not l:
            break



print(VD)
with open('invalid.txt','w') as data:
    data.write(str(VD))
