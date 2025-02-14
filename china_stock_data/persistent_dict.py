import json
import os
from .config import API_DICT_FILE, APP_DICT_FILE
from threading import Lock
from typing import Any, Dict

class PersistentDict:
    def __init__(self, filename: str):
        if not filename:
            raise ValueError("Filename cannot be empty")
        
        self.filename = os.path.abspath(filename)
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.data: Dict[str, Any] = self._load_dict_from_file()
        self.lock = Lock()

    def _load_dict_from_file(self) -> Dict[str, Any]:
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print(f"Warning: Could not decode JSON from {self.filename}. Starting with an empty dictionary.")
            return {}

    def _save_dict_to_file(self) -> None:
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        with self.lock:
            return self.data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        with self.lock:
            self.data[key] = value
            self._save_dict_to_file()  # 立即保存到文件

    def delete(self, key: str) -> None:
        with self.lock:
            if key in self.data:
                del self.data[key]
                self._save_dict_to_file()  # 立即保存到文件


    def get_all(self) -> Dict[str, Any]:
        with self.lock:
            return self.data.copy()

    def has(self, key: str) -> bool:
        with self.lock:
            return key in self.data

    def update(self, new_data: Dict[str, Any]) -> None:
        with self.lock:
            self.data.update(new_data)
            self._changed = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # 不需要在这里保存，因为每次修改都会立即保存
    
# 使用示例保持不变
api_dict = PersistentDict(API_DICT_FILE)
app_dict = PersistentDict(APP_DICT_FILE)
