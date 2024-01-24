from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler
)

from helper.framex import FrameXHelper
from utils.bisect import Bisect


# Telegram Bot API Token
TOKEN: Final = "6749505123:AAHWRFuHrVETnbWz_Bh6-aWlVquve6gG8SU"
USERNAME: Final = "Rocket Launch"
helper = FrameXHelper()

bisect = None
video = None


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(context._chat_id, "Hello, World!")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(context._chat_id, "Game started, enjoy!")
    global bisect, video
    video = helper.get_video()
    bisect = Bisect(video.frames)
    await image_command(update, context)


async def image_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bisect, video
    if bisect and video:
        frame = helper.get_video_frame(video.name, bisect.mid_point)

        buttonsMenu = [
            [InlineKeyboardButton("Has been launched! 🚀", callback_data="launched")],
            [InlineKeyboardButton("Not launched yet ⏳", callback_data="not_launched")],
        ]
        keyboard_markup = InlineKeyboardMarkup(buttonsMenu)
        await context.bot.send_photo(
            chat_id=context._chat_id, 
            photo=frame,
            caption=f"Step {bisect.current_step}\nHas the rocket been launched?",
            reply_markup=keyboard_markup
        )
    else:
        await start_command(update, context)


def handle_response(text: str):
    processed: str = text.lower()

    if processed == "hello":
        return "Hi!"

    return "I don't understand you."


async def handle_message(update: Update, context: ContextTypes. DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if USERNAME in text:
            new_text: str = text. replace(USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await context.bot.send_message(chat_id=context._chat_id, text=response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


async def handle_launched(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Launched")
    global bisect, video
    bisect.process_step(True)
    if bisect.is_finished():
        bisect = None
        video = None
        await context.bot.send_message(context._chat_id, "Congratulations, you found the launch frame!")
    else:
        await image_command(update, context)


async def handle_not_launched(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Not launched")
    global bisect, video
    bisect.process_step(False)
    if bisect.is_finished():
        bisect = None
        video = None
        await context.bot.send_message(context._chat_id, "Congratulations, you found the launch frame!")
    else:
        await image_command(update, context)


if __name__ == '__main__':
    print('Starting bot...')

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('hello', hello_command))
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('image', image_command))

    # Messages
    # app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(CallbackQueryHandler(handle_launched, pattern="launched"))
    app.add_handler(CallbackQueryHandler(handle_not_launched, pattern="not_launched"))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    app.run_polling(poll_interval=0.5)
