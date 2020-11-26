import json

with open("users.json", "r") as json_file:
    users_dict = json.load(json_file)
print(len(users_dict["users"]))
