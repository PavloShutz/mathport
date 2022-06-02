"""Module for saving data in json for telegram bot"""
import json
from pathlib import Path


class ConfigureData:

    @staticmethod
    def __load_file_data(new_data: dict) -> None:
        """Loads data into json file."""
        path = Path('new.json')
        data = json.loads(path.read_text(encoding='utf-8'))
        data['info'].append(new_data)
        path.write_text(json.dumps(data, sort_keys=False,
                                   indent=4, ensure_ascii=False),
                        encoding='utf8')

    def save_info(self, user_name: str, user_message: str,
                  bot_message: str, current_time: str) -> None:
        """Saves info about user message and bot reply-message."""
        new_data = {'user_name': user_name,
                    'user_message': user_message,
                    'bot_message': bot_message,
                    'time_added': current_time}
        self.__load_file_data(new_data)
