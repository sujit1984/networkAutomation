#str1 = ''

with open("sample_txt_file.txt", 'r') as f:
    content = f.read().splitlines()
    str1 = '\n'.join(content)
print(str1)