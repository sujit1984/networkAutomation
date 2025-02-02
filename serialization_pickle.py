"""
This program shows the serialization and deserialization of data using python
"""

import pickle



friends = {"Dan":[20, "London", 8923492232], "Maria": [30,"Madrid", 61232332]}

with open("friends.dat", 'wb') as file:
    pickle.dump(friends,file)

with open("friends.dat", 'rb') as fr:
    obj = pickle.load(fr)
    print(type(obj))
    print(obj)