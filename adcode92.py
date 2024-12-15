f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
line = f.readline()
line = list(line)
start = 0
end = len(line)-1
value_start = 0
value_end = len(line)//2
counter = 0
space = 0
freespace = []
sum = 0
blocks_managed = 0
blocks_in_total = (len(line)//2) + 1
isFile = True
files = []
counter = 0
index_file = blocks_in_total-1
file_value = 0
index_free = 0
while (blocks_managed != blocks_in_total):
    if(isFile):
        files.append((counter, (counter + int(line[start])), int(line[start]), index_file, file_value))
        counter += int(line[start])
        start += 1
        index_file -= 1
        isFile = False
        blocks_managed += 1
        file_value += 1
    else:
        freespace.append((counter, (counter + int(line[start])), int(line[start]), index_free))
        counter += int(line[start])
        start += 1
        index_free += 1
        isFile = True

files.reverse()
new_files = []
for file in files:
    new_files.append(file)

for file in new_files:
   # print(file)
    (file_start, file_end, file_size, index_file, file_value) = file 
    for free in freespace:
        (free_start, free_end, free_size, index_free) = free
        if free_size >= file_size and (file_start > free_start):
            files[index_file] = (free_start, free_start + file_size, file_size, index_file, file_value)
            freespace[index_free] = (free_start + file_size, free_end, free_size-file_size, index_free )
           # print(files[index_file])
            break

sum = 0
for file in files:
    (file_start, file_end, file_size, index_file, file_value) = file
    while file_end > file_start:
        #print("calc " + str(file_start) + " " + str(file_value))
        sum += file_start * file_value
        file_start += 1
print(sum)





