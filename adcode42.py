f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
lines = f.readlines()
a = [[],[],[]]
i = 3
sum = 0
for j in range(len(lines[0])+6):
    a[0].append('0')
for j in range(len(lines[0])+6):
    a[1].append('0')
for j in range(len(lines[0])+6):
    a[2].append('0')
for line in lines:
    a.append(['0','0','0'])
    for j in range(len(line)):
        a[i].append(line[j])
    a[i].append('0')
    a[i].append('0')
    a[i].append('0')
    a[i].append('0')
    i += 1
a.append([])
for j in range(len(lines[0])+6):
    a[i].append('0')
a.append([])
for j in range(len(lines[0])+6):
    a[i+1].append('0')
a.append([])
for j in range(len(lines[0])+6):
    a[i+2].append('0')
a.append([])
for j in range(len(lines[0])+6):
    a[i+3].append('0')

for x in range(2,i):
    for y in range(2, len(a)-2):
        if(a[x][y] == 'A'):
            if(a[x-1][y-1] == 'M' and a[x+1][y-1] == 'M' and a[x-1][y+1] == 'S' and a[x+1][y+1] == 'S'):
                sum += 1
            if(a[x-1][y-1] == 'S' and a[x+1][y-1] == 'S' and a[x-1][y+1] == 'M' and a[x+1][y+1] == 'M'):
                sum += 1
            if(a[x-1][y-1] == 'M' and a[x+1][y-1] == 'S' and a[x-1][y+1] == 'M' and a[x+1][y+1] == 'S'):
                sum += 1
            if(a[x-1][y-1] == 'S' and a[x+1][y-1] == 'M' and a[x-1][y+1] == 'S' and a[x+1][y+1] == 'M'):
                sum += 1
            
print(a)
print(sum)    