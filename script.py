"""Script to get info from JSON file"""

import json
from pathlib import Path

path = Path("new.json")
data = json.loads(path.read_text(encoding='utf-8'))
users = []
i = 0
while i < len(data['info']):
    users.append(data['info'][i]['user_name'])
    i += 1

text = f"""
1) Type 'username' to get user who made operations. Available users:
{sorted(set(users))}
2) Type 'day' to know who and what messages were sent to bot
"""

days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

parameters = """
1) user messages;
2) bot messages.
"""

while True:
    print(text)
    user_input = input(">>>")
    if user_input.lower() == 'q':
        next_user_input = input("Are you sure you want to quit? [y/N]")
        if next_user_input.lower() == 'y':
            break
    elif user_input.lower() not in days:
        print(parameters)
        next_user_input = input(">>>")
        if next_user_input == '1' or next_user_input.lower() == 'user messages':
            i = 0
            for i in range(len(data['info'])):
                if data['info'][i]['user_name'].lower() == user_input.lower():
                    print(f"{i+1}) User\'s message: {data['info'][i]['user_message']}",
                          f"\nUser\'s message added: {data['info'][i]['time_added']}\n")
        elif next_user_input == '2' or next_user_input.lower() == 'bot messages':
            i = 0
            for i in range(len(data['info'])):
                if data['info'][i]['user_name'].lower() == user_input.lower():
                    print(f"Bot\'s message: {data['info'][i]['bot_message']}",
                          f"\nBot\'s message added: {data['info'][i]['time_added']}")
    elif user_input.lower() in days:
        i = 0
        for i in range(len(data['info'])):
            if ''.join(data['info'][i]['time_added'].split('-')[0]).lower() == user_input.lower():
                print(f"{i+1}) User: {data['info'][i]['user_name']}\nUser message: {data['info'][i]['user_message']}\n")
