"""
This program eliminates the empty lines and spaces in a given text file.
"""

# reading the file in a list
with open('sample_txt_file1.txt.txt') as f:
    content_list = f.readlines()

# create a new list eliminating the elements that are empty strings or contain only spaces
tmp_list = [line for line in content_list if line.strip() != '']
print(tmp_list)

# write to a new file
with open('sample_file_without_blanks.txt', 'w') as f:
    f.write(''.join(tmp_list))