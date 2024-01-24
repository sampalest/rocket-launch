############
# Handlers #
############

from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from core import commands as cmd


def set_handlers(app: Application):
    # Project
    app.add_handler(CommandHandler('start', cmd.start_command, block=False))
    app.add_handler(CommandHandler('play', cmd.play_command, block=False))
    app.add_handler(CommandHandler('health', cmd.health_command, block=False))

    # Error
    app.add_error_handler(cmd.error, block=False)

    # Messages
    app.add_handler(
        CallbackQueryHandler(cmd.launched_command, pattern="launched", block=False)
    )
    app.add_handler(
        CallbackQueryHandler(cmd.not_launched_command, pattern="not_launched", block=False)
    )
