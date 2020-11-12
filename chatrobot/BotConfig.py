import os
class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DB_URL = os.environ.get("DATABASE_URL", None)
    API_HASH = os.environ.get("API_HASH", None)
    API_ID = int(os.environ.get("APP_ID", 6))
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "^/")
    DUMB_CHAT = int(os.environ.get("DUMB_CHAT", False))
    CUSTOM_START = os.environ.get("CUSTOM_START", None)
    CUSTOM_IMG = os.environ.get("CUSTOM_IMG", "https://1.bp.blogspot.com/-y__OlAp2LKg/X61N-u7FwiI/AAAAAAAAAAM/mX7EkEau4dw9vrCugZ61zo_i5SAbSM3jwCLcBGAsYHQ/s480/Photo_1603283479401.png")
