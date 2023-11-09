with open('file_handling/newfile.txt','w') as file:
    # file.write('This is a new file created')
    file.writelines(['This is a new file created', '\nThis is another line']) # add \n for new line

with open('file_handling/newfile.txt','a') as file: # added mode = 'a' to avoid rewrite
     file.writelines(['\nThis is a new file created', '\nThis is another line']) 