"""Script to get info from JSON file"""


import json
from pathlib import Path


path = Path("new.json")
data = json.loads(path.read_text(encoding='utf-8'))
users = [data['info'][i]['user_name'] for i in range(len(data['info']))]
text = f"""
1) Type 'username' to get user who made operations. Available users:
{sorted(set(users))}
2) Type 'day' to know who and what messages were sent to bot
"""

days = ('monday', 'tuesday',
        'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

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
    elif user_input.lower() not in days \
            and user_input.lower() in sorted(set([i.lower() for i in users])):
        print(parameters)
        next_user_input = input(">>>")
        if next_user_input == '1' \
                or next_user_input.lower() == 'user messages':
            for item in range(len(data['info'])):
                if data['info'][item]['user_name'].lower() \
                        == user_input.lower():
                    print(f"{item + 1}) User\'s message: "
                          f"{data['info'][item]['user_message']}",
                          f"\nUser\'s message added: "
                          f"{data['info'][item]['time_added']}\n")
        elif next_user_input == '2' \
                or next_user_input.lower() == 'bot messages':
            for item in range(len(data['info'])):
                if data['info'][item]['user_name'].lower()\
                        == user_input.lower():
                    print("Bot\'s message: "
                          f"{data['info'][item]['bot_message']}",
                          f"\nBot\'s message added: "
                          f"{data['info'][item]['time_added']}")
    elif user_input.lower() in days:
        for item in range(len(data['info'])):
            message_for_this_day = \
                ''.join(data['info'][item]['time_added'].split('-')[0]).lower()
            if message_for_this_day \
                    == user_input.lower():
                print(f"{item + 1}) User: {data['info'][item]['user_name']}\n"
                      f"User message: {data['info'][item]['user_message']}\n")
    else:
        print('Hey, type or name, like "Pasha", '
              'or type any day you want, for example "Monday".')
