# ROCKET-LAUNCH
A simple game using a Telegram bot.

![rocket-logo](docs/images/rocket.svg)

## Description

This bot is a simple game in which you'll have to identify the frame where the SpaceX Falcon Heavy rocket is launched.
The bot will show you images, and you just have to respond whether the rocket has been launched or not.

This code is only a Poc to show a simple Telegram bot using Python.

## Instalation
1. Clone.
2. Generate a Telegram bot using `@botfather` or start `@SamRocketBot` (if still exists).
3. Make a `.env` using `.env.example`.
4. Execute `make run`.

## Config
You need to create a `.env` file using the following variables:

- **TELEGRAM_TOKEN**: You Telegram bot token.
- **BOT_NAME**: Bot username for example: SamRocketLaunch.

There's another options, but it's defined by default.

- **LOG_LEVEL**: Level of logs.
- **BOT_LANG**: Set your language.
- **TELEGRAM_POLLING**: Time of telegram polling. (See Telegram API for more info)

You can configure another languages using `./src/resources/lang/<<your_language>>` and set it in `BOT_LANG`.

This project is so simple to use that you don't need to know anything else. 😃

## Contributing

If you want to contributing [click here](docs/contributing.md).

### TODO

- Implement REDIS
- Tests

## Libraries

* coloredlogs: https://coloredlogs.readthedocs.io/en/latest/
* python-telegram-bot: https://python-telegram-bot.org/
* requests: https://requests.readthedocs.io/en/latest/

## Author
Samuel Palomo Esteban