# That's one way of reading files.
# file = open('Files/news.txt')
# print(file.readlines())
# file.close()


# A better way

# File modes:
# @see File modes https://www.geeksforgeeks.org/reading-writing-text-files-python/

# @see Path lib https://docs.python.org/3/library/pathlib.html

# r => read only (default);
# r+ => read and write
# w => write only;
# w+ => write and read;
# a => append only
# a+ => read and append
try:
    with open('news.txt', mode='r') as file:
        #new_text = file.write('A lovely day in London!')
        print(file.read())
except FileNotFoundError as err:
    print('File does not exit. Verify the file name')
