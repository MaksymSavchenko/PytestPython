file = open('test.txt')
#print(file.read(11)) # read all contents of the file

#print(file.readline()) # read one single line
#print(file.readline())



# print line by line using readline method
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

for line in file.readlines(): # check loops section
    print(line)

file.close()