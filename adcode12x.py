f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
little = f.readlines()
lines = []
for line in little:
    if '\n' in line:
        line = line[:-1]
        print(line)
    line = list(line)
    lines.append(line)

y_max = len(lines)-1
x_max = len(lines[0])-1

sum = 0
sum2 = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] != '#':
            area = 0
            omkreds = 0
            stack = [(x,y)]
            region = lines[y][x]
            visited = [(x,y)] 
            lines[y][x] = '*'
            lineseg = []
            while stack != []:
                (x1,y1) = stack.pop()
             
                area += 1
                
                if y1 - 1 >= 0 and lines[y1-1][x1] == region:
                    stack.append((x1,y1-1))
                    visited.append((x1,y1-1))
                    lines[y1-1][x1] = '*'
                else:
                    if y1 - 1 >= 0 and lines[y1-1][x1] == '*':
                        1+1
                    else:
                        omkreds += 1
                        lineseg.append(((x1,y1),(x1,y1-1), "up"))
                
                if x1 - 1 >= 0 and lines[y1][x1-1] == region:
                    stack.append((x1-1,y1))
                    visited.append((x1-1,y1))
                    lines[y1][x1-1] = '*'
                else:
                    if x1 - 1 >= 0 and lines[y1][x1-1] == '*':
                        1+1
                    else:
                        omkreds += 1
                        lineseg.append(((x1,y1),(x1-1,y1), "left"))
                
                if y1 + 1 <= y_max and lines[y1+1][x1] == region:
                    stack.append((x1,y1+1))
                    visited.append((x1,y1+1))
                    lines[y1+1][x1] = '*'
                else:
                    if y1 + 1 <= y_max and lines[y1+1][x1] == '*':
                        1+1
                    else:
                        omkreds += 1
                        lineseg.append(((x1,y1),(x1,y1+1), "down"))
                
                if x1 + 1 <= x_max and lines[y1][x1+1] == region:
                    stack.append((x1+1,y1))
                    visited.append((x1+1,y1))
                    lines[y1][x1+1] = '*'
                else:
                    if x1 + 1 <= x_max and lines[y1][x1+1] == '*':
                        1+1
                    else:
                        omkreds += 1
                        lineseg.append(((x1,y1),(x1+1,y1), "right"))
            
            print("area")
            print(area)
            print("omkreds")
            print(omkreds)
            print("a * o")
            print(area * omkreds)
             
            sum += area * omkreds
            print(sum)
            for (a,b) in visited:
                lines[b][a] = '#'
            while lineseg != []:
                ((x1,y1),(x2,y2), dir) = lineseg.pop(0)
                for(((cx1,cy1),(cx2,cy2),cdir)) in lineseg:
                    if dir ==  cdir:
                        if dir == "up" and (((cx1-1,cy1),(cx2-1,cy2)) == ((x1,y1),(x2,y2)) or ((cx1+1,cy1),(cx2+1,cy2)) == ((x1,y1),(x2,y2)) ):
                            omkreds -= 1
                        if dir == "down" and (((cx1-1,cy1),(cx2-1,cy2)) == ((x1,y1),(x2,y2)) or ((cx1+1,cy1),(cx2+1,cy2)) == ((x1,y1),(x2,y2)) ):
                            omkreds -= 1
                        if dir == "left" and (((cx1,cy1-1),(cx2,cy2-1)) == ((x1,y1),(x2,y2)) or ((cx1,cy1+1),(cx2,cy2+1)) == ((x1,y1),(x2,y2)) ):
                            omkreds -= 1
                        if dir == "right" and (((cx1,cy1-1),(cx2,cy2-1)) == ((x1,y1),(x2,y2)) or ((cx1,cy1+1),(cx2,cy2+1)) == ((x1,y1),(x2,y2)) ):
                            omkreds -= 1
            sum2 += area * omkreds
                        


            
print(sum)
print(sum2)  