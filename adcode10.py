f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
little = f.readlines()
lines = []
for line in little:
    if '\n' in line:
        line = line[:-1]
        print(line)
    inter = []
    for c in line:
        inter.append(int(c))
    lines.append(inter)

y_max = len(lines)-1
x_max = len(lines[0])-1

sum = 0
sum2 = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 0:
            stack = [(0,x,y)]
            reached = []
            while stack != []:
                (value, x1, y1) = stack.pop()
                if value != 9:
                    if y1 - 1 >= 0 and lines[y1-1][x1] == value+1:
                        stack.append((value+1,x1,y1-1))
                    if x1 - 1 >= 0 and lines[y1][x1-1] == value+1:
                        stack.append((value+1,x1-1,y1))
                    if y1 + 1 <= y_max and lines[y1+1][x1] == value+1:
                        stack.append((value+1,x1,y1+1))
                    if x1 + 1 <= x_max and lines[y1][x1+1] == value+1:
                        stack.append((value+1,x1+1,y1))
                elif value == 9 and not ((x1,y1) in reached) :
                    sum += 1
                    sum2 += 1
                    reached.append((x1,y1))
                else:
                    sum2 += 1
print(lines)
print(sum)
print(sum2)
                 
            
                    


