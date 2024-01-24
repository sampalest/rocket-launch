# Contributing to Rocket-Launch

Thank you for your interest in contributing to the project! Your help is invaluable to grow and improve the community. Before you start, please take a moment to review the following guidelines.

## How to Contribute

1. [Fork](https://help.github.com/en/articles/fork-a-repo) the repository to your GitHub account.
2. Clone your fork to your local machine.
3. Create a branch for your contribution.
4. Make your changes and ensure to follow the project's style guides and conventions.
5. Perform local tests to ensure your contribution works correctly.
6. Commit your changes.
7. Push to your branch.
8. Open a [Pull Request](https://help.github.com/en/articles/creating-a-pull-request) to the main branch of the project.

## General Guidelines

- **Style Guides:** Follow the project's style guides. Ensure your code is consistent with the existing style.
- **Testing:** Add tests for any new features or bug fixes you implement.
- **Documentation:** Update the documentation accordingly to reflect your changes.

## Project Structure

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

## Start the project locally

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

### Next Steps

- Implement REDIS
- Tests