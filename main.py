import json

with open("network.json","r") as file:
    data = json.load(file)
    
users = data["users"]

user_map = {}
for user in users:
    user_map[user["id"]] = user
    
for user in users:
    CR_id = user["id"]
    CR_name = user["name"]
    CR_friends = set(user["friends"])
    
    suggest = set()
    
    for friend_id in CR_friends:
        friend = user_map.get(friend_id)
        
        if friend:
            for mutual in friend["friends"]:
                if mutual!= CR_id and mutual not in CR_friends:
                    suggest.add(mutual)
                    
    print(f"\nthis is current user {CR_name}")
    
    if suggest:
        for uid in suggest:
            print("-",user_map[uid]["name"])
            
    else:
        print("none")
