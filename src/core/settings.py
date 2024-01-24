import os

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
    "30"
))
