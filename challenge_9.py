"""
Write a Python script that reads the file in a dictionary.
The words in the file will be the dictionary keys and the length of each word the corresponding values.
"""

with open("american-english.txt", "r") as file:
    content = file.read().splitlines()
    #print(content)

    dictionary = {x:len(x) for x in content}
    #print(dictionary)

"""
Challenge 10 - Consider the dictionary file from the previous challenge.

Write a Python script that finds the first 100 longest words in the file.

"""


view = sorted(dictionary.items(), key = lambda x: x[1],reverse=True)
print(view[:100])