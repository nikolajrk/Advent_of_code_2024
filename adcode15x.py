f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
little = f.readlines()
grid = []
for line in little:
    if '\n' in line:
        line = line[:-1]
    grid.append(list(line))
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
            

        elif grid[s_y-1][s_x] == 'O':
            row = 2
            while True:
                if grid[s_y-row][s_x] == 'O':
                    row += 1
                    continue
                elif grid[s_y-row][s_x] == '.':
                    grid[s_y-row][s_x] = 'O'
                    grid[s_y][s_x] = '.'
                    grid[s_y-1][s_x] = '@'
                    s_y = s_y-1
                    break
                else:
                    break
    if order == 'v':
        if grid[s_y+1][s_x] == '.':
            f.write("met . \n")
            
            grid[s_y][s_x] = '.'
            grid[s_y+1][s_x] = '@'  
            s_y = s_y+1
        elif grid[s_y+1][s_x] == 'O':
            f.write("met O \n")
            row = 2
            while True:
                if grid[s_y+row][s_x] == 'O':
                    row += 1
                    continue
                elif grid[s_y+row][s_x] == '.':
                    grid[s_y+row][s_x] = 'O'
                    grid[s_y][s_x] = '.'
                    grid[s_y+1][s_x] = '@'
                    s_y = s_y+1
                    break
                else:
                    break
    if order == '>':
        if grid[s_y][s_x+1] == '.':
            grid[s_y][s_x] = '.'
            grid[s_y][s_x+1] = '@'
            s_x = s_x+1
        elif grid[s_y][s_x+1] == 'O':
            row = 2
            while True:
                if grid[s_y][s_x+row] == 'O':
                    row += 1
                    continue
                elif grid[s_y][s_x+row] == '.':
                    grid[s_y][s_x+row] = 'O'
                    grid[s_y][s_x] = '.'
                    grid[s_y][s_x+1] = '@'
                    s_x = s_x+1
                    break
                else:
                    break
    if order == '<':
        if grid[s_y][s_x-1] == '.':
            grid[s_y][s_x] = '.'
            grid[s_y][s_x-1] = '@'
            s_x = s_x-1
        elif grid[s_y][s_x-1] == 'O':
            row = 2
            while True:
                if grid[s_y][s_x-row] == 'O':
                    row += 1
                    continue
                elif grid[s_y][s_x-row] == '.':
                    grid[s_y][s_x-row] = 'O'
                    grid[s_y][s_x] = '.'
                    grid[s_y][s_x-1] = '@'
                    s_x = s_x-1
                    break
                else:
                    break
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
        if grid[y][x] == 'O':
            sum += 100 * y + x
print(sum)