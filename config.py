import os
from dotenv import load_dotenv

load_dotenv()

NUMBER_OF_ROOMS = 3

KEY = os.environ.get("KEY")
SECRET = os.environ.get("SECRET")

BACKUP_KEY = os.environ.get("BACKUP_KEY")
BACKUP_SECRET = os.environ.get("BACKUP_SECRET")
