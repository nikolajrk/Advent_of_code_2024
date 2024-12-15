f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
little = f.readlines()
grid = []
for line in little:
    sun = ""
    if '\n' in line:
        line = line[:-1]
    for c in line:
        if c == '@':
            sun += '@.'
        elif c == 'O':
            sun += '[]'
        else:
            sun += c
            sun += c
    print(sun)
    grid.append(list(sun))
    
print(grid)
f = open("C:/Users/nikol/Downloads/adcode2.txt", 'r')
orders = []
sun = ""
little = f.readlines()
for line in little:
    if '\n' in line:
        line = line[:-1]
    sun += line
print(sun)
orders = list(sun)
print(orders)
s_x = 0
s_y = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '@':
            s_x = x
            s_y = y
        
f = open("C:/Users/nikol/Downloads/adcode3.txt", 'w')
for order in orders:
    print("stuff happening")
    f.write(" : xn = ")
    f.write(str(s_x))
    f.write(" : sy = ")
    f.write(str(s_y))
    f.write('\n')
    if order == '^':
        if grid[s_y-1][s_x] == '.':
            grid[s_y][s_x] = '.'
            grid[s_y-1][s_x] = '@'
            s_y = s_y-1
            

        elif grid[s_y-1][s_x] == '[' or grid[s_y-1][s_x] == ']':
            row = 2
            stack = []
            if grid[s_y-1][s_x] == '[':
                stack = [(s_y-2,s_x),(s_y-2,s_x+1)]
                thingstochange = [(s_y-1,s_x, grid[s_y-1][s_x]),(s_y-1,s_x+1,grid[s_y-1][s_x+1])]
                
            else:
                stack = [(s_y-2,s_x),(s_y-2,s_x-1)]
                thingstochange = [(s_y-1,s_x, grid[s_y-1][s_x]),(s_y-1,s_x-1, grid[s_y-1][s_x-1])]
                
            
            hitwall = False
            n = 0
            
            while stack != []:
                
                (qy,qx) = stack.pop()
                
                print("whileloop1")
                if grid[qy][qx] == '#':
                    hitwall = True
                    break
                elif grid[qy][qx] == '.':
                    continue
                elif grid[qy][qx] == '[':
                    stack.append((qy-1,qx))
                    stack.append((qy-1,qx+1))
                    thingstochange.append((qy,qx, grid[qy][qx]))
                    thingstochange.append((qy,qx+1, grid[qy][qx+1]))
                elif grid[qy][qx] == ']':
                    stack.append((qy-1,qx))
                    stack.append((qy-1,qx-1))
                    thingstochange.append((qy,qx,grid[qy][qx]))
                    thingstochange.append((qy,qx-1, grid[qy][qx-1]))
            
            if not hitwall:
                thingstochange.reverse()
                print(thingstochange)
                listofvisited = []
                for (qy,qx,thing) in thingstochange:
                    if not((qy,qx,thing) in listofvisited):
                        grid[qy-1][qx] = thing
                        grid[qy][qx] = '.'
                    listofvisited.append((qy,qx,thing))
                grid[s_y][s_x] = '.'
                grid[s_y-1][s_x] = '@'  
                s_y = s_y-1
      
    if order == 'v':
        if grid[s_y+1][s_x] == '.':
            f.write("met . \n")
            
            grid[s_y][s_x] = '.'
            grid[s_y+1][s_x] = '@'  
            s_y = s_y+1
        
        elif grid[s_y+1][s_x] == '[' or grid[s_y+1][s_x] == ']':
            row = 2
            stack = []
            if grid[s_y+1][s_x] == '[':
                stack = [(s_y+2,s_x),(s_y+2,s_x+1)]
                thingstochange = [(s_y+1,s_x, grid[s_y+1][s_x]),(s_y+1,s_x+1,grid[s_y+1][s_x+1])]
            else:
                stack = [(s_y+2,s_x),(s_y+2,s_x-1)]
                thingstochange = [(s_y+1,s_x, grid[s_y+1][s_x]),(s_y+1,s_x-1, grid[s_y+1][s_x-1])]
            
            hitwall = False
            n = 0
            while stack != []:
                (qy,qx) = stack.pop()
                print("whileloop2")
                if grid[qy][qx] == '#':
                    hitwall = True
                    break
                elif grid[qy][qx] == '.':
                    continue
                elif grid[qy][qx] == '[':
                    stack.append((qy+1,qx))
                    stack.append((qy+1,qx+1))
                    thingstochange.append((qy,qx, grid[qy][qx]))
                    thingstochange.append((qy,qx+1, grid[qy][qx+1]))
                elif grid[qy][qx] == ']':
                    stack.append((qy+1,qx))
                    stack.append((qy+1,qx-1))
                    thingstochange.append((qy,qx,grid[qy][qx]))
                    thingstochange.append((qy,qx-1, grid[qy][qx-1]))
            
            if not hitwall:
                thingstochange.reverse()
                print(thingstochange)
                listofvisited = []
                for (qy,qx,thing) in thingstochange:
                    if not((qy,qx,thing) in listofvisited):
                        grid[qy+1][qx] = thing
                        grid[qy][qx] = '.'
                    listofvisited.append((qy,qx,thing))
                grid[s_y][s_x] = '.'
                grid[s_y+1][s_x] = '@'  
                s_y = s_y+1


    if order == '>':
        if grid[s_y][s_x+1] == '.':
            grid[s_y][s_x] = '.'
            grid[s_y][s_x+1] = '@'
            s_x = s_x+1
        elif grid[s_y][s_x+1] == '[':
            row = 2
            hitwall = False
            stuffx = s_x +1
            stuffx2 = 0
            while True:
                print("whileloop3")
                if grid[s_y][s_x + 1 + row] == '[':
                    row += 2
                elif grid[s_y][s_x + 1 + row] == '#':
                    hitwall = True
                    break
                elif grid[s_y][s_x + 1 + row] == '.':
                    stuffx2 = s_x + 1 + row
                    break
            if not hitwall:
                i = stuffx + 1
                a = True
                while i <= stuffx2:
                    if a:
                        grid[s_y][i] = '['
                        a = False
                    else:
                        grid[s_y][i] = ']'
                        a = True
                    i += 1
                grid[s_y][s_x] = '.'
                grid[s_y][s_x+1] = '@'
                s_x = s_x+1

    if order == '<':
        if grid[s_y][s_x-1] == '.':
            grid[s_y][s_x] = '.'
            grid[s_y][s_x-1] = '@'
            s_x = s_x-1
        elif grid[s_y][s_x-1] == ']':
            row = 2
            hitwall = False
            stuffx = s_x -1
            stuffx2 = 0
            q = 0
            while True:
                print("whileloop4")
                print(q)
                q += 1
                print(grid[s_y][s_x - 1 - row])
                if grid[s_y][s_x - 1 - row] == ']':
                    row += 2
                elif grid[s_y][s_x - 1 - row] == '#':
                    hitwall = True
                    break
                elif grid[s_y][s_x - 1 - row] == '.':
                    stuffx2 = s_x - 1 - row
                    break
            if not hitwall:
                i = stuffx - 1
                a = False
                while i >= stuffx2:
                    if a:
                        grid[s_y][i] = '['
                        a = False
                    else:
                        grid[s_y][i] = ']'
                        a = True
                    i -= 1
                grid[s_y][s_x] = '.'
                grid[s_y][s_x-1] = '@'
                s_x = s_x-1
    f.write(order)
    f.write(" : xn = ")
    f.write(str(s_x))
    f.write(" : sy = ")
    f.write(str(s_y))
    f.write('\n')
    for lin in grid:
        sun = ""
        for c in lin:
            sun += c
        
        f.write(sun + '\n')


            
    
    

for lin in grid:
    sun = ""
    for c in lin:
        sun += c
    print(sun)

sum = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '[':
            sum += 100 * y + x
print(sum)