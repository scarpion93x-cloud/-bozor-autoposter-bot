import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID", "97550738"))

    DATABASE_URL = os.getenv("DATABASE_URL")

    GROUPS = [
        "@quyichirchiq_oqqorgon_bozor"
    ]

config = Config()
