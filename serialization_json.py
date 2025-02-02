"""
This program shows how serialization works with json
"""
import json

friends = {"Dan":[20, "London", 8923492232], "Maria": [30,"Madrid", 61232332]}

#dump method

with open("friends.json", "w") as f:
    json.dump(friends,f,indent=4)

json_string = json.dumps(friends, indent=4)
print(json_string)