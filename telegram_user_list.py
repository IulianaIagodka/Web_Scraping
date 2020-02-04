from fileinput import input
from time import sleep
from telethon import TelegramClient, events, sync
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = "put here your id"
api_hash = "put here your hash"
target_group = "watchmen"
phone_number = "+380954290857"

client = TelegramClient("session_name", api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    myself = client.sign_in(phone_number, input('Enter code: '))
# If .sign_in raises PhoneNumberUnoccupiedError, use .sign_up instead
# If .sign_in raises SessionPasswordNeeded error, call .sign_in(password=...)
# You can import both exceptions from telethon.errors.


def get_users(a_channel):
    offset = 0
    limit = 100
    all_participants = []
    while True:
        participants = client.invoke(GetParticipantsRequest(
            a_channel, ChannelParticipantsSearch(''), offset, limit, hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)
        sleep(1)
    return all_participants


def print_users(a_users):
    for user in a_users:
        print(user.username)


print_users(get_users(target_group))

#print("Fetching Members...")
#all_participants = []
#all_participants = client.get_participants(target_group, aggressive=True)

