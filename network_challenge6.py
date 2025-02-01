"""
Write a Python program to count the number of lines, words, and characters in a text file.
This is similar to the Linux `wc` command. Create a function, if possible.
"""

def wc(filename):
    with open(filename,'r') as file:
        content = file.read().splitlines()
        file.seek(0)
        words = len(file.read().split())
        file.seek(0)
        characters=len(file.read())
        #print(characters)
        print(characters)
        #print(words)
        lines = len(content)
        print(words)
        print(lines)

        print(f"There are {lines} lines, {words} words and {characters} characters in the {filename}")


wc('sample_txt_file2.txt')