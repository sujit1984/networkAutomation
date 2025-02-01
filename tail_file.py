"""
This program emaulates the unix's tail command. The function tail takes in 2 inputs - filename and n, where n is the
number of lines. On running the program , the tail function extracts the last n lines from the input file and
prints them
"""

def tail(filename, n):
    with open(filename, 'r') as file:
        content = file.read().splitlines()
        last = content[len(content) - n:]
        # print(last)
        # concateneting the list back into a string
        my_str = '\n'.join(last)
        print(my_str)


tail("sample_txt_file2.txt",5)
