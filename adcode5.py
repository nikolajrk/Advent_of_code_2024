f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
rules = []

line = f.readline()

while len(line) == 6:
    [a,b] = line.split('|')
    b = b[:-1]
    rules.append((a,b))
    line = f.readline()
sum1 = 0
sum2 = 0
sum3 = 0
lines = f.readlines()
for line in lines:
    line = line[:-1]
    pages = line.split(',')
    arr = []
    broken = []
    is_right = True
    for p in pages:
        for pp in arr:
            for (a,b) in rules:
                if p == a and pp == b:
                    is_right = False
                    broken.append((a,b))
        arr.append(p)
    if(is_right):
        sum1 += int(arr[len(arr)//2])
    if(not is_right):
        new = pages.copy()
        res = []
        for i in range(len(new)):
            res.append(0)
        i = 0
        for a in new:
            res[i] = (0,a)
            for b in new:
                if not a == b:
                    if (a,b) in rules:
                        (sum,ind) = res[i]
                        res[i] = (sum+1, a)
            i += 1
        res.sort()
        (stuff, stuff2) = res[len(res)//2] 
        sum3 += int(stuff2)



    if(not is_right):
        shit = True
        while shit:
            for (a,b) in broken:
                c = pages.index(a)
                d = pages.index(b) 
                pages[c] = b
                pages[d] = a
            arr = []
            broken = []
            is_right = True
            for p in pages:
                for pp in arr:
                    for (a,b) in rules:
                        if p == a and pp == b:
                            is_right = False
                            broken.append((a,b))
                arr.append(p)
            if is_right:
                shit = False
        
        sum2 += int(pages[len(pages)//2])
        print(int(pages[len(pages)//2]))
        print(pages)
        
    



print(sum1)
print(sum2)
print(sum3)




