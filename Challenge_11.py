"""

"""
import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_letters:
    letters[c] = 0

print(letters)

with open("american-english.txt", 'r') as file:
    for word in file:
        for char in string.ascii_letters:
            letters[char]+=word.count(char)

print(letters)


'''
### Challenge#12 Change the solution from the previous challenge so that the script considers 
all letters lowercase (it makes no distinction between lower and uppercase letters).

'''

alphabets = dict()
for c in string.ascii_lowercase:
     alphabets[c] = 0

with open("american-english.txt", 'r') as file:
    for w in file:
        for char in string.ascii_lowercase:
            alphabets[char]+=w.lower().count(char)

print(alphabets)

'''
Challenge #13
Continue the previous challenge and find the 3 most frequently used letters in all English Words.
You should get: ('e', 67681), ('s', 50872), ('i', 50818)
'''

sort_by_value = dict(sorted(alphabets.items(), key=lambda item: item[1],reverse=True))

out = {k: sort_by_value[k] for k in list(sort_by_value)[:3]}
print(out)
