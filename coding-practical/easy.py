'''
# Print lines containing ERROR
LOG_FILE= "/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/app.log"
with open(LOG_FILE) as f:
    for line in f:
        if "ERROR" in line:
            print(line)
'''

#Count total number of lines in a file
LOG_FILE= "/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/app.log"
count = 0
with open(LOG_FILE) as f:
    for line in f:
        count += 1
    print(count)    