from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import Dispatcher, CommandHandler
from flask import Flask, request
from callbacks import (
    start,
    users,
    shop,
    smartphone,
    phone,
    add_cart,
    cart,
    clear_cart,
)


TOKEN = "5980348926:AAFW6kZ4j-aJk-SvLs657PJYqb4RoFNS5d4"

print('TOKEN:', TOKEN)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, None, workers=0)


app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "webhook is running...!"
    
    if request.method == 'POST':
        
        body = request.get_json()
        
        update = Update.de_json(body, bot)

        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(CommandHandler('users', users))
        dp.add_handler(MessageHandler(Filters.text('🛍 Shop'), shop))
        dp.add_handler(MessageHandler(Filters.text('🛒 Cart'), cart))
        dp.add_handler(CallbackQueryHandler(smartphone, pattern='brend:'))
        dp.add_handler(CallbackQueryHandler(phone, pattern='phone:'))
        dp.add_handler(CallbackQueryHandler(add_cart, pattern='add:'))
        dp.add_handler(CallbackQueryHandler(clear_cart, pattern='clear'))

        dp.process_update(update)

        return {'message': 'ok'}


if __name__ == '__main__':
    app.run(debug=True)
