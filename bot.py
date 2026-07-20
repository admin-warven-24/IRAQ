from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1AZWarzgBuwesKhPGe92ETUTVwJDmSyA0TupvFCVgJCXy15CjV1MJp5jL3heCfSqobh2__blMqKan0IzeH-5d8oDDK16EiWUS2TScg5FPHJ4SG1eiQMGNzwDW7NMgZWuy4fyICDeB0-iXep3IjFVPQ2Xi78Dk0y26D6oCpiYqUKYWAnbbNXIGFoYq3dskRY1MYWWQI32oKDYkHХ0Нр3МVacmzGqrsPErLRHITWMcGYkgSjNpSzY_sQjuq_tSdqTYzViQOZWSRBFeihtpIz5ny1d4tj8nG6XxTQs81fMguhbTUuRF_t5-TOKRD9vYrs_gm2t1tGI5nwnSuE7HFvg6-XctTmSLKC4A="

SOURCE_CHANNEL = "@WarnisxCcScrap"
TARGET_CHANNEL = "@kurdiraq7272"

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message
    new_text = msg.text or ""
    new_text = new_text.replace("@About_Warnisx", "@kurdiraq7272")
    new_text = new_text.replace("@Warnisx", "@kurdiraq7272")

    if msg.media:
        data = await msg.download_media(file=bytes)
        await client.send_file(TARGET_CHANNEL, data, caption=new_text, formatting_entities=msg.entities)
    else:
        await client.send_message(TARGET_CHANNEL, new_text, formatting_entities=msg.entities)

print("Bot is running...")
client.start()
client.run_until_disconnected()
