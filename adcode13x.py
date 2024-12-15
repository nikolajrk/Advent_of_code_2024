f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
little = f.readlines()
counter = 0
inputs = []
ax = ""
ay = ""
bx = ""
by = ""
for line in little:
    if '\n' in line:
        line = line[:-1]
        
    if counter == 0:
        inter = line.split(' ')
  
        ax = int(inter[2][2:][:-1])
      
        ay = int(inter[3][2:])
  
        counter += 1
    elif counter == 1:
        inter = line.split(' ')
   
        bx = int(inter[2][2:][:-1])

        by = int(inter[3][2:])

        counter += 1
    elif counter == 2:

        inter = line.split(' ')

        xt = int(inter[1][2:][:-1])
        yt = int(inter[2][2:])
        inputs.append( ( (ax,ay) , (bx,by), (xt+10000000000000,yt+10000000000000)) )
        counter += 1
    elif counter == 3:
        counter = 0
    
sum = 0



for ((a1,a2),(b1,b2) ,(c1,c2)) in inputs:
    determinant = a1 * b2 - b1 * a2
    print(determinant)
    
    if determinant == 0:
        print("deter^")
        shit = 0
        fuck = 0
        if(c1 % b1 == 0 and c2 % b2 == 0):
            shit = c1 // b1
        if(c1 % a1 == 0 and c2 % a2 == 0):
            fuck = c1 // a1
        if fuck == 0:
            sum += shit
        elif shit == 0:
            sum += fuck
        elif (fuck * 3 < shit):
            sum += 3 * fuck
        else: 
            sum += shit
    elif((c1*b2 - c2*b1) % determinant == 0) and ((c2*a1 - c1*a2) % determinant == 0) :
            x = (c1*b2 - c2*b1)/determinant
            y = (c2*a1 - c1*a2)/determinant

            sum += 3 * x + y       
    else:
        print(determinant)

print(sum)

