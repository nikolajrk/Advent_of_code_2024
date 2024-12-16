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
        found = False
        for a in coordinates:
            x2 = 0
            for b in a :
                if (x1,y1) != (x2,y2):
                    if b != '.':
                        new_x = x2 + (x2-x1)
                        new_y = y2 + (y2-y1)
          
                        if new_x <= x_max and new_x >= 0 and new_y <= y_max and new_y >= 0:
                            if b == coordinates[new_y][new_x]:
                                found = True
                                coord2[y1][x1] = '#'
                                break
                x2 += 1
            
            if found:
                sum += 1
                break
            y2 +=1
        x1 += 1
    y1 +=1
print(sum)
for line in coord2:
    shit = ""
    for c in line:
        shit += c
    print(shit)
                
        
        
