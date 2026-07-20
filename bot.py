from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1AZWarzgBuyFQd57gW4J-XbkOy6fp4NDaIshg8b21ufEj5d2iDV9QV2Kgb6XWIJ9PNAOB4ZWLbz36aW-FDKnrmq_fAtICRuj_51HhvLs4NvzuTk3VpZBz5K0vP9ark2797VaktricuGKGD5HU7Gn8Hn30YTd6E-DwUt7tfw2SqVJ_P6AdVab81Sxw5yLytxZhbcntdVLNRVc-WofkSWwj_UQyQkPIKK1GlFaLqRbbt45UaRho7s63BT4iukyNfywBdyRPrbWEelLHAdcdzRtFXiLzO6iGzd4EDX3av9oy2u7VO0JbbQ1CKJfCHQ4-8vbMfifE3SNryrzVtX1GNzw_TVZPVnW5NI8="

SOURCE_CHANNEL = "@WarnisxCcScrap"
TARGET_CHANNEL = "@kurdiraq7272"
# ===================================

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message
    new_text = msg.text or ""
    new_text = new_text.replace("@About_Warnisx", "@kurdiraq7272")
    new_text = new_text.replace("@Warnisx", "@kurdiraq7272")

    if msg.media:
        data = await msg.download_media(file=bytes)
        await client.send_file(
            TARGET_CHANNEL,
            data,
            caption=new_text,
            formatting_entities=msg.entities
        )
    else:
        await client.send_message(
            TARGET_CHANNEL,
            new_text,
            formatting_entities=msg.entities
        )

print("Bot is running...")
client.start()
client.run_until_disconnected()
