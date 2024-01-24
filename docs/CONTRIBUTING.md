# Contributing
This is a game but maybe you want to add new functionality or just use the project structure to create your own TG Bot, so I'm going to explain the structure.

## Structure

### Core
The core functionality

#### Handlers
Here is defined the actions of your bot. For example `start`, `hello`, `health`...

#### Commands
You have to define logic of your bot handlers. For example if you have defined a `start` in your handler, here have to develop the `start` functionality. 

#### Settings
Here is the config of all project. It's like a constant file.

### Storage
The storage is responsible of save in RAM the state of players.
(This will be Redis in the future)

### Services
Here is the business logic that you will implement in your commands.

### Helpers
The name already indicates that. 🙂

### Model
Define your models.

### Resources

#### Lang
Here in this folder you can define another languages. (fr, es, etc).
By default is english (en).

## Start the project locally.

1. Install pipenv in your machine (https://pipenv-es.readthedocs.io/es/latest/)

```bash
pipenv install
pipenv shell
python main.py
```

## Debug using VSCode
A little help for debug using VSCode.
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Main",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/main.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "TELEGRAM_POLLING": "0.5",
                "TELEGRAM_TOKEN": "your-token",
                "TELEGRAM_BOT_USERNAME": "RocketLaunch",
                "LOG_LEVEL" : "INFO"
            }
        }
    ]
}

```