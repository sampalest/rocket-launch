import json
import logging
import os

import coloredlogs

logger = logging.getLogger(__name__)


# Project Constants

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
BOT_NAME = os.getenv("BOT_NAME", "Telegram Bot")
BOT_LANG = os.getenv("BOT_LANG", "en")

# Init

coloredlogs.install(level=LOG_LEVEL)

# Telegram Constants

TELEGRAM_POLLING = float(os.getenv("TELEGRAM_POLLING", "0.5"))
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# FrameX Constants

FRAMEX_BASE_URL = os.getenv(
    "FRAMEX_BASE_URL",
    "https://framex-dev.wadrid.net/api/"
)
FRAMEX_VIDEO_NAME = os.getenv(
    "FRAMEX_VIDEO_NAME",
    "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
)
FRAMEX_REQUEST_TIMEOUT = int(os.getenv(
    "FRAMEX_REQUEST_TIMEOUT",
    "60"
))

# Get Strings

try:
    with open(f"src/resources/lang/{BOT_LANG}.json", "r") as f:
        STRINGS = json.load(f)

except (FileNotFoundError):
    logger.error(f"Language {BOT_LANG} not found. Using English.")
    with open("src/resources/lang/en.json", "r") as f:
        STRINGS = json.load(f)
