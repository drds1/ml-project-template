import os
from dotenv import load_dotenv
import json
from pathlib import Path
from settings.settings import settings

class Config:
    def __init__(self, config_file=None):
        config_dir = Path(__file__).parent / "config_jsons"
        default_path = config_dir / "default.json"
        self.data = json.loads(default_path.read_text())

        if config_file:
            custom_path = config_dir / config_file
            if custom_path.exists():
                custom_data = json.loads(custom_path.read_text())
                self.data.update(custom_data)

    def __getattr__(self, name):
        return self.data.get(name)