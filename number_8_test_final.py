inFile = open('C:\\temp\\jenners.txt','r')
output = open('C:\\temp\\output.txt','w')
line = inFile.readline()
read_value = line
while (read_value != ''):
    print(read_value)
    output.write(read_value)
    line = inFile.readline()
    read_value = line
print("The last Line has been read!")
inFile.close()
output.close()