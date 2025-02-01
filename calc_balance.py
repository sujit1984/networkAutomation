"""
This program reads the content of the file transaction.txt and determines the current balance of the account.
"""
balance = 0
with open('transaction.txt', 'r') as file:
    content = file.read().splitlines()
    deposit, withdrawal = 0, 0
    for item in content:
        trans = item.split(':')
        if trans[0] == 'D':
            deposit+=int(trans[1])
        else:
            withdrawal+=int(trans[1])

balance = deposit - withdrawal
print(balance)
