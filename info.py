# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6717382350"))
API_ID = int(getenv("API_ID", "26162072"))
API_HASH = str(getenv("API_HASH", "ba25181c01b50d945748801b6c8b6ecc"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://rebelbotz22:vNcEEoNvSQ33d44K@cluster0.oj1hu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href=''>{file_name} Telegram : @RM_Botz\n\nForward the file before Downloading.</a></b>",
    )
)
