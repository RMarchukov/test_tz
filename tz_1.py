from telethon import TelegramClient
import asyncio
import pymorphy2
from config import SESSION_NAME, API_ID, API_HASH


client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def main():
    json_names = {}
    male_users = []
    female_users = []
    unknown_gender_users = []
    try:
        await client.start()
        group_username = input("Введіть назву групи: ")
        group_entity = await client.get_entity(group_username)
        participants = await client.get_participants(group_entity)

        for participant in participants:
            if participant.username is None:
                json_names.update({participant.first_name:
                    {
                        "name": participant.first_name,
                        "last_name": participant.last_name
                    }
                })
            else:
                json_names.update({participant.username:
                    {
                        "name": participant.first_name,
                        "last_name": participant.last_name
                    }
                })
        print(json_names)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await client.disconnect()

    morph = pymorphy2.MorphAnalyzer()

    for username, name in json_names.items():
        if " " in name["name"]:
            res = name["name"].split(" ")[0]
        else:
            res = name["name"]

        parsed_word = morph.parse(res)[0]
        if parsed_word.tag.gender == "femn":
            female_users.append(username)
        elif parsed_word.tag.gender == "masc":
            male_users.append(username)
        else:
            unknown_gender_users.append(username)

    with open("filtered_files/male.txt", "w") as male_file:
        male_file.write("\n".join(male_users))

    with open("filtered_files/female.txt", "w") as female_file:
        female_file.write("\n".join(female_users))

    with open("filtered_files/unknown_gender.txt", "w") as unknown_gender_file:
        unknown_gender_file.write("\n".join(unknown_gender_users))


if __name__ == '__main__':
    asyncio.run(main())
