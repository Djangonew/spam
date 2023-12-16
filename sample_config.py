from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    False  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = "6329227771:AAGJEjUD05mKhFg_ViVaflP9B7GB2zZpjnI"
    SUDOERS = [1748872441]
    NSFW_LOG_CHANNEL = -1002005183024
    SPAM_LOG_CHANNEL = -1002005183024
    ARQ_API_KEY = "PKLSXO-SMGXLS-KGHVKD-UMYHCS-ARQ"  # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("BOT_TOKEN")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL"))
    ARQ_API_KEY = env.get("ARQ_API_KEY")
