from telegram import Bot

TOKEN = "5980348926:AAFW6kZ4j-aJk-SvLs657PJYqb4RoFNS5d4"

bot = Bot(token=TOKEN)

def get_info():
    print(bot.get_webhook_info())


def delete():
    print(bot.delete_webhook())


def set():
    url = 'https://azizbek0780.pythonanywhere.com/webhook'
    print(bot.set_webhook(url=url))

set()
