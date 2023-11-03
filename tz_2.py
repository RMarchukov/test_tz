import logging
import os
from captcha.image import ImageCaptcha
from telethon.sync import TelegramClient, events
from PIL import Image
from random import randint
from config import API_ID, API_HASH, API_TOKEN

script_directory = os.path.abspath(os.path.dirname(__file__))
captcha_images_directory = os.path.join(script_directory, 'captcha_images')

if not os.path.exists(captcha_images_directory):
    os.makedirs(captcha_images_directory)

logging.basicConfig(level=logging.DEBUG)

client = TelegramClient('tz_2', API_ID, API_HASH).start(bot_token=API_TOKEN)


def get_captcha() -> dict[str | None]:
    numbers = []
    captcha = ImageCaptcha()
    for i in range(5):
        numbers.append(str(randint(0, 9)))

    data = "".join(numbers)
    image_data = captcha.generate(data)

    image_file_path = 'captcha_images/captcha.png'
    with open(image_file_path, 'wb') as image_file:
        image = Image.open(image_data)
        image.save(image_file, format='PNG')
    return {"data": data, "file": image_file_path}


cap = get_captcha()


@client.on(events.NewMessage(pattern="/start"))
async def welcome_func(event):
    channel = event.peer_id
    if cap["file"] is not None:
        try:
            await client.send_file(channel, cap["file"], caption="Hello! Please repeat this numbers: ")
            await client.delete_messages(channel, [event.message.id, ])
        except TypeError as e:
            print(f"An error occurred: {e}")
    else:
        await event.respond("Bad request...")
        await client.delete_messages(channel, [event.message.id, ])


@client.on(events.NewMessage)
async def check_captcha(event):
    channel = event.peer_id
    if event.raw_text != cap["data"] and cap["file"] is not None:
        await client.send_file(channel, cap["file"], caption=f"Not right. Please repeat this numbers: ")
        await client.delete_messages(channel, [event.message.id, ])
    elif event.raw_text == cap["data"]:
        await event.respond(f"Hello, {channel.user_id}!")
        await client.delete_messages(channel, [event.message.id, ])
        cap["data"] = ""
        cap["file"] = None


@client.on(events.NewMessage(pattern="join"))
async def handler(event):
    group_entity = await client.get_entity("pogromista")
    participants = await client.get_participants(group_entity)
    print(group_entity.id)
    for participant in participants:
        print(participant)


# @client.on(events.NewMessage(pattern="public_join"))
# async def join_to_public_channel(event):
#     await client(InputChannel('ПМПСС'))
#     print(event.raw_text)
#
#
# @client.on(events.NewMessage(pattern="private_join"))
# async def join_to_private_channel(event):
#     channel = event.peer_id
#     res = client(InputChannel('ПМПСС'))
#     print(res)


client.run_until_disconnected()
