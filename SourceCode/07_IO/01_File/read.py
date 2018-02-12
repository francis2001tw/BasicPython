# read file

# # [POINT 1]
# with open('MyFile.txt') as f:
#     readData = f.read()
#     print(readData)

# [POINT 2]
with open('MyFile.txt') as f:
    lines = f.readlines()

    for line in lines:
        print(line, end='')
