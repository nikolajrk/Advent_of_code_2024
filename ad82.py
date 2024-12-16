f = open("C:/Users/nikol/OneDrive/Desktop/Adventofcode/input.txt")
lines = f.readlines()
coordinates = []

for line in lines:
    if '\n' in line:
        line = line[:-1]
    coordinates.append(list(line))
print(coordinates)

coord2 = []
for line in coordinates:
    coord2.append(line.copy())
y1 = 0
x1 = 0
y2 = 0
x2 = 0
y_max = len(coordinates)-1
x_max = len(coordinates[0])-1
found = False
sum = 0
for row in coordinates:
    x1 = 0
    for element in row:
        y2 = 0
        if(coordinates[y1][x1]) != '.':
            for a in coordinates:
                x2 = 0
                for b in a :
                    if (x1,y1) != (x2,y2):
                        if b == coordinates[y1][x1]:
                            inside = True
                            new_x = x2 + (x2-x1)
                            new_y = y2 + (y2-y1)
                            while inside:
                                if new_x <= x_max and new_x >= 0 and new_y <= y_max and new_y >= 0:
                                    coord2[new_y][new_x] = '#'
                                    new_x += (x2-x1)
                                    new_y += (y2-y1)
                                else:
                                    inside = False

                    x2 += 1
                
                
                y2 +=1
        x1 += 1
    y1 +=1
print(sum)
for line in coord2:
    shit = ""
    for c in line:
        shit += c
        if(c != '.'):
            sum += 1
    print(shit)
print(sum)
                
        
        
