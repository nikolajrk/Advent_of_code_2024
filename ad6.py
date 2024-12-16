f = open("C:/Users/nikol/OneDrive/Desktop/Adventofcode/input.txt")
lines = f.readlines()
coordinates = []
y = 0
x = 0
start1 = (0,0, (0,0), 0, True)
for line in lines:
    line = line[:-1]
    coordinates.append(list(line))
    x = 0
    for c in list(line):
        if c == '^':
            start1 = (x,y, (0,-1), 1, True)
            coordinates[y][x] = 'X'
        elif c == '>':
            start1 = (x,y,(1,0), 1, True)
            coordinates[y][x] = 'X'
        elif c == '<':
            start1 = (x,y,(-1,0), 1, True)
            coordinates[y][x] = 'X'
        elif c == 'v':
            start1 = (x,y,(0,1), 1, True)
            coordinates[y][x] = 'X'
        x += 1
    y +=1 
shit = True
x_max = len(coordinates[0])-1
y_max = len(coordinates)-1
def turn(coord):
    if coord == (0,-1):
        return (1,0)
    elif coord == (1,0):
        return (0,1)
    elif coord == (0,1):
        return (-1,0)
    elif coord == (-1,0):
        return (0,-1)
    else:
        return coord

def walk(start):
    (x, y, direc, sum, shit) = start
    (move_x, move_y) = direc
    if (x >= 1 and x <= x_max-1 and y >= 1 and y <= y_max-1):
        coord = coordinates[y+move_y][x+move_x]
        if  coord == 'X':
            coordinates[y][x] = 'X'
            return x+move_x, y+move_y, direc, sum, shit
        elif coord == '#':
            return x, y, turn(direc),sum, shit
        elif coord == '.':
            coordinates[y][x] = 'X'
            sum += 1
            return x+move_x, y+move_y, direc, sum, shit
    else:
        shit = False
        return x, y, direc, sum, shit

    
walking = True
sum = 1
start2 = start1
while walking:
    (x, y, direc, sum, shit) = walk(start1)
    walking = shit
    start1 = (x,y,direc, sum, shit)
sum = 1
output = ""
q = 0
for list in coordinates:
    q = 0
    for c in list:
        if c == 'X':
            sum += 1
        output += c
    output += '\n'
    q += 1
print(output)
print(sum)
xc = 0
yc = 0
ways = 0
for list in coordinates:
    (x2,y2,f,r,e) = start2
    xc = 0
    for c in list:
        if (x2,y2) != (xc,yc):
            thing = coordinates[yc][xc]
            coordinates[yc][xc] = '#'
            counter = 0
            walking = True
            sum = 1
            start1 = start2
            while walking:
                counter += 1
                (x, y, direc, sum, shit) = walk(start1)
                walking = shit
                start1 = (x,y,direc, sum, shit)
                if counter > 35000:
                    print("loop")
                    print(xc)
                    print(yc)
                    ways += 1
                    break
            coordinates[yc][xc] = thing
        xc += 1
    yc +=1
print(ways)
