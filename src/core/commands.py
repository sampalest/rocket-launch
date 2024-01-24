############
# Commands #
############

import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from core.settings import STRINGS
from helpers.framex import FrameXHelper
from models.video import Video
from services.bisect import Bisect
from storage import Storage

logger = logging.getLogger(__name__)
stg = Storage()


# General commands

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f'Update {update} caused error {context.error}')


# Bot commands

async def health_command(_: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Health check command.
    """
    await context.bot.send_message(context._chat_id, STRINGS["health"])


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(context._chat_id, STRINGS["start_1"])
    await context.bot.send_message(context._chat_id, STRINGS["start_2"])


async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Play command.
    """

    # First instances
    framex = FrameXHelper()
    video = framex.get_video()
    bisect = Bisect(video.frames)

    stg.delete_bot_id(context._chat_id)
    stg.add_bot_instances(context._chat_id, "framex", framex)
    stg.add_bot_instances(context._chat_id, "video", video)
    stg.add_bot_instances(context._chat_id, "bisect", bisect)

    await image_command(update, context)


async def image_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(context._chat_id, STRINGS["loading"])

    # Get API session
    framex: FrameXHelper = stg.get_bot_instance(context._chat_id, "framex")

    # Get video instance
    video: Video = stg.get_bot_instance(context._chat_id, "video")

    # Get bisect instance
    bisect: Bisect = stg.get_bot_instance(context._chat_id, "bisect")

    if bisect and video:
        frame = framex.get_video_frame(video.name, bisect.mid_point)

        buttonsMenu = [
            [InlineKeyboardButton(STRINGS["button_ok"], callback_data="launched")],
            [InlineKeyboardButton(STRINGS["button_ko"], callback_data="not_launched")],
        ]
        keyboard_markup = InlineKeyboardMarkup(buttonsMenu)
        await context.bot.send_photo(
            chat_id=context._chat_id,
            photo=frame,
            caption=STRINGS["step_question"] % bisect.current_step,
            reply_markup=keyboard_markup
        )
    else:
        await start_command(update, context)


# Answer commands

async def launched_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    launched: bool = context.match.string == 'launched'
    await button_command(launched, update, context)


async def not_launched_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    launched: bool = context.match.string == 'launched'
    await button_command(launched, update, context)


async def button_command(launched: bool, update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get API session
    framex: FrameXHelper = stg.get_bot_instance(context._chat_id, "framex")

    # Get video instance
    video: Video = stg.get_bot_instance(context._chat_id, "video")

    # Get bisect instance
    bisect: Bisect = stg.get_bot_instance(context._chat_id, "bisect")
    bisect.process_step(launched)

    if bisect.is_finished():
        frame = framex.get_video_frame(video.name, bisect.limit_right)
        stg.delete_bot_id(context._chat_id)

        await context.bot.send_photo(
            chat_id=context._chat_id,
            photo=frame,
            caption=STRINGS["found"]
        )
    else:
        await image_command(update, context)
