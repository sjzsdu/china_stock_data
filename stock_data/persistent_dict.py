import json
import os
from .config import API_DICT_FILE, APP_DICT_FILE
class PersistentDict:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._load_dict_from_file()

    def _load_dict_from_file(self):
        """Load the dictionary from a file if it exists."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def _save_dict_to_file(self):
        """Save the dictionary to a file."""
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def get(self, key, default=None):
        """Get a value from the dictionary."""
        return self.data.get(key, default)

    def set(self, key, value):
        """Set a value in the dictionary and save to file."""
        self.data[key] = value
        self._save_dict_to_file()

    def delete(self, key):
        """Delete a key from the dictionary and save to file."""
        if key in self.data:
            del self.data[key]
            self._save_dict_to_file()

    def get_all(self):
        """Get the entire dictionary."""
        return self.data

api_dict = PersistentDict(API_DICT_FILE)
app_dict = PersistentDict(APP_DICT_FILE)
