from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from echo.config import MY_TOKEN, BASE_URL

def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Hey! Send me something',
    )

def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = "Your ID={}\nYour message - {}".format(chat_id, update.message.text)
    bot.send_message(
        chat_id=chat_id,
        text=text,
    )


def main():
    bot = Bot(
        token=MY_TOKEN,
        base_url=BASE_URL
    )
    updater = Updater(
        bot=bot,
    )
    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
