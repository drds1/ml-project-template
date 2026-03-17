import os
from dotenv import load_dotenv
import json
from pathlib import Path


load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_ORG = os.getenv("GITHUB_ORG")

SNOWFLAKE_CONFIG = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),
}


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
