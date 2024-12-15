f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
lines = f.readlines()
a = []
b = []
for line in lines:
    spli = line.split("   ")
    a.append(int(spli[0]))
    b.append(int(spli[1]))

i = 0

sum = 0
while i < len(a):
    j = 0
    for nr in b:
        if nr == a[i]:
            j += 1
    sum += j * a[i]
    i += 1
print(sum)