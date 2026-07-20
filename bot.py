import re
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1AZWarzgBuyFQd57gW4J-XbkOy6fp4NDaIshg8b21ufEj5d2iDV9QV2Kgb6XWIJ9PNAOB4ZWLbz36aW-FDKnrmq_fAtICRuj_51HhvLs4NvzuTk3VpZBz5K0vP9ark2797VaktricuGKGD5HU7Gn8Hn30YTd6E-DwUt7tfw2SqVJ_P6AdVab81Sxw5yLytxZhbcntdVLNRVc-WofkSWwj_UQyQkPIKK1GlFaLqRbbt45UaRho7s63BT4iukyNfywBdyRPrbWEelLHAdcdzRtFXiLzO6iGzd4EDX3av9oy2u7VO0JbbQ1CKJfCHQ4-8vbMfifE3SNryrzVtX1GNzw_TVZPVnW5NI8="

SOURCE_CHANNEL = "@WarnisxCcScrap"
TARGET_CHANNEL = "@kurdiraq7272"
# ===================================

def format_card_data(text):
    # دەستنیشانکردنی ژمارەی کارت
    cc_match = re.search(r'(\d{16})\|(\d{2})\|(\d{4})\|(\d{3,4})', text)
    if cc_match:
        cc, month, year, cvv = cc_match.groups()
        bin_num = cc[:6]
    else:
        # ئەگەر کارت نەدۆزرایەوە، سەرپەڕ و کۆتایی بە ناوی خوازراو
        return f"KURD Scrapper by @warven_24\n\n{text}\n\nDeveloped By @warven_24"

    # دەرهێنانی Bank, Country, Type
    bank_match = re.search(r'Bank:\s*(.+)', text, re.IGNORECASE)
    country_match = re.search(r'Country:\s*(.+)', text, re.IGNORECASE)
    type_match = re.search(r'Type:\s*(.+)', text, re.IGNORECASE)

    bank = bank_match.group(1).strip() if bank_match else "N/A"
    country = country_match.group(1).strip() if country_match else "N/A"
    card_type = type_match.group(1).strip() if type_match else "N/A"

    # فۆرماتی خوازراو (تەنها دەق، بەبێ لینک)
    formatted = f"""KURD Scrapper by @warven_24

CC: `{cc}|{month}|{year}|{cvv}`
BIN: `{bin_num}`
Bank: {bank}
Country: {country}
Type: {card_type}

Developed By @warven_24"""

    # ئەگەر کات لە کۆتاییدا هەبوو، زیادیشی بکە (بەبێ لینک)
    extra_match = re.search(r'(\d+\s+\d+:\d+\s+[AP]M)$', text)
    if extra_match:
        formatted += f"\n\n{extra_match.group(1)}"
    
    return formatted

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message
    original_text = msg.text or ""

    # ========== فلترکردن ==========
    # 1. ئەگەر میدیا (وێنە/ڤیدیۆ/فایل) هەبوو، پشتگوێی بخرێت
    if msg.media:
        return
    
    # 2. ئەگەر لینک (URL) لە ناو دەقەکەدا هەبوو، پشتگوێی بخرێت
    url_pattern = r'https?://[^\s]+|www\.[^\s]+|t\.me/[^\s]+|telegram\.me/[^\s]+'
    if re.search(url_pattern, original_text):
        return
    # ================================

    # پەیامەکە بپڕۆسێسە و بنێرە (تەنها دەق، بەبێ میدیا)
    new_text = format_card_data(original_text)
    await client.send_message(TARGET_CHANNEL, new_text)

print("Bot is running... (تەنها پەیامی تێکستی بەبێ لینک و وێنە دەنێردرێت)")
client.start()
client.run_until_disconnected()
