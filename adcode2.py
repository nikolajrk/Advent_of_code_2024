f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
lines = f.readlines()
a = []
sum = 0
for line in lines:
    numbers = line.split(" ")
    last = int(numbers[0])
    increasing = True
    decreasing = True
    safe = 1
    print(line)
    for q in numbers:
        n = int(q)
        if(n > last):
            decreasing = False
        elif (n < last):
            increasing = False
        if(abs(n - last)>3 or (n==last)):
            safe -= 1
        last = n
    if (increasing or decreasing) and safe == 0:
        sum +=1

print(sum)
