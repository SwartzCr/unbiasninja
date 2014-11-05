from twython import Twython
import json

def auth():
    with open("access.json", 'r') as f:
        db = json.load(f)
    return Twython(db["API_Key"], db["API_Secret"], db["Access_Token"], db["Access_Token_Secret"])


def get_friends(twitter, user_id):
    cursor = -1
    out = []
    while cursor != -1:
        resp = twitter.get_friends_ids(user_id=user_id)
        out += resp['ids']
        cursor = resp['next_cursor']
    return out

def get_friends_names(twitter, user_list):
    out = []
    # split user_list into groups of 100
    for num in range(0, len(user_list), 100):
    # call lookup_user for each of these
        out += [user["name"] for user in twitter.lookup_user(user_id=user_list[num:num+100])]
    # return a list of usernames
    return out

def save(names_list):
    with open(""+user_id+".json", 'w') as f:
        json.dump(names_list, f)

def main(user_id):
    twitter = auth()
    user_list = get_friends(twitter, user_id)
    names_list = get_friends_names(twitter, user_list)
    save(names_list)
