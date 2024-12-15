f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
lines = f.readlines()
a = []
b = []
for line in lines:
    spli = line.split("   ")
    a.append(int(spli[0]))
    b.append(int(spli[1]))

a.sort()
b.sort()
i = 0
sum = 0
while i < len(a):
    sum += abs(a[i]-b[i])
    i += 1
print(sum)