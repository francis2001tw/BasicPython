# write file

# # [POINT 1]
# with open('MyNote.txt', 'w') as f:
#     f.write('ID: 123\n')
#     f.write('Name: Frank\n')

# [POINT 2]
with open('MyNote.txt', 'a') as f:
    f.write('ID: 456\n')
    f.write('Name: Tom\n')
