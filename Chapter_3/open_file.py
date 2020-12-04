# import os
# os.getcwd()
# os.chdir('Chapter_3')

data = open('sketch.txt')
print(data.readline(), end='')
print(data.readline(), end='')

# rewind the cursor
data.seek(0)

for each_line in data:
    print(each_line, end='')

data.close()
