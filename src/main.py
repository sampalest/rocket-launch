import logging

from telegram.ext import Application
from core.settings import BOT_NAME, TELEGRAM_TOKEN, TELEGRAM_POLLING
from core.handlers import set_handlers


logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info(f"Starting {BOT_NAME} bot...")

    # App definition
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Set handlers
    set_handlers(app)

    # Polls the bot
    app.run_polling(poll_interval=TELEGRAM_POLLING)
