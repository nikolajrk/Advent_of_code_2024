f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
lines = f.readlines()
a = []
sum = 0
for line in lines:
    numbersq = line.split(" ")

    for i in range(len(numbersq)):
        if(i == 0):
            last = int(numbersq[1])
        else:
            last = int(numbersq[0])
        safe = 1
        increasing = True
        decreasing = True
        for q in range(len(numbersq)):
                if(q != i):
                    n = int(numbersq[q])
                    if(n > last):
                        decreasing = False
                    elif (n < last):
                        increasing = False
                    if(abs(n - last)>3 or (n==last)):
                        safe -= 1
                    last = n
        if (increasing or decreasing) and safe == 0:
            sum +=1
            break;            
                    
                

print(sum)
