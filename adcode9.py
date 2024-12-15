f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
line = f.readline()
line = list(line)
start = 0
end = len(line)-1
value_start = 0
value_end = len(line)//2
counter = 0
space = 0
freespace = False
sum = 0
intermedi = int(line[end])
while(value_start <= value_end):
    if(not freespace) and value_start < value_end:
        counter = int(line[start])
        while counter > 0:
            counter -= 1
            print("calcnor: " + str(space) + " " + str(value_start))
            sum += space * value_start
            print("Sum: " + str(sum))
            space += 1
        start += 1
        value_start += 1
        freespace = True
    elif(not freespace):
        counter = intermedi
        while counter > 0:
            counter -= 1
            print("calcnor: " + str(space) + " " + str(value_start))
            sum += space * value_start
            print("Sum: " + str(sum))
            space += 1
        start += 1
        value_start += 1
        freespace = True
    else:
        counter = int(line[start])
        while counter > 0 and (value_start < value_end):
            if intermedi > 0:
                counter -= 1
                print("calcEnd: " + str(space) + " " + str(value_end))
                sum += space * value_end
                print("Sum: " + str(sum))
                space += 1
                intermedi -= 1
            elif value_start < value_end-1:
                end -= 2
                intermedi = int(line[end])
                value_end -= 1
            else:
                break
        freespace = False
        start += 1
print(sum)




