"""
This is a program to read the content of the file macs.txt and extract the macaddresses separately and write them into
another file -- each macAddress in its own line
"""

with open("macs.txt", 'r') as file:
    macs = file.read().split()
#print(macs)

unique_macs = list(set(macs))
print(unique_macs)

# with open('uniq_macs.txt','w') as wfile:
#     for item in unique_macs:
#         wfile.write("\n".join(unique_macs))
with open('uniq_macs.txt', 'w', newline='') as f:
    for mac in unique_macs:
        f.write(f'{mac}\n')
