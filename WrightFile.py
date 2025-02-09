# read the file and store all the lines in a list
# reverse the list
with open('test.txt', 'r') as reader: #r - read only w -rw
    content = reader.readlines()
#    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)