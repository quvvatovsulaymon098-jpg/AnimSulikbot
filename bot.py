import telebot
import requests

TOKEN = "9161711250:AAF4RQ1N0kyqsO05qYE3u7HlQU1uzcjnG6Y"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Салом! 👋 Акси аниме фирист, ман номашро мегӯям!")

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, "Ҷустуҷӯ карда истодаам... 🔍")
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
        r = requests.post("https://api.trace.moe/search", params={"url": file_url}).json()
        result = r['result'][0]
        name = result['filename']
        sim = round(result['similarity'] * 100, 1)
        bot.send_message(message.chat.id, f"📌 Ном: {name}\n⭐ Монанди: {sim}%\n🎞️ Қисм: {result['episode']}")
    except Exception as e:
        bot.send_message(message.chat.id, "Хатогӣ шуд, боз акси дигар фирист 😅")

print("Бот кор мекунад...")
bot.polling()
