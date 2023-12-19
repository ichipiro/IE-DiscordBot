import os
from dotenv import load_dotenv


load_dotenv()
EXTENSIONS = [
    # extensions here
    "cogs.ping",
    "cogs.reminder",
]
TOKEN = os.environ["TOKEN"]
REMINDER_CHANNEL_ID = int(os.environ["REMINDER_CHANNEL_ID"])
