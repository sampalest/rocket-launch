from typing import Any

###########
# Storage #
###########

import logging

logger = logging.getLogger(__name__)


class Storage:
    def __init__(self):
        self._storage = {}

    def add_bot_instances(self, chat_id: str, name: str, instance: object) -> None:
        """
        Add a bot instance to the storage.
        :param chat_id: The chat id.
        :param name: The name of the instance.
        :param instance: The instance.
        """
        self._storage.setdefault(chat_id, {})
        self._storage[chat_id][name] = instance

    def get_bot_instances(self, chat_id: int) -> Any | None:
        """
        Get all bot instances of a user.
        :param chat_id: The chat id.
        :return: The bot instances.
        """
        try:
            return self._storage[chat_id]
        except KeyError:
            logger.error(f"Chat {chat_id} not found in storage.")
            return None

    def get_bot_instance(self, chat_id: int, name: str) -> Any | None:
        """
        Get a bot instance of a user.
        :param chat_id: The chat id.
        :param name: The name of the instance.
        :return: The bot instance.
        """
        try:
            return self._storage[chat_id][name]
        except KeyError:
            logger.error(f"Chat {chat_id} not found in storage.")
            return None

    def delete_bot_id(self, chat_id: int) -> None:
        """
        Delete a bot instance of a user.
        :param chat_id: The chat id.
        """
        self._storage.pop(chat_id, None)


# TODO: Implement storage with Redis using TTL because of memory! This is just a PoC.
