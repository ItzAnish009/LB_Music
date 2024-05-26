import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "26108237"))
API_HASH = getenv("API_HASH", "b69fac6842079a15c7b51b16f70cf77e")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6571199121:AAGyGOXDBfA17LPYsTzZX9_8AoTPCbl20JI")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Anishkhamrui76:Anishkhamrui76@cluster0.ezysgve.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001745060879"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "1822479202"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "anishmusic76")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-3d7d7f18-527f-44b9-b150-6ed19a92bf9b")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/ItzAnish009/LB_Music/edit/master/config.py", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")
SUPPORT_CHAT = getenv("SUPPORT_GROUP")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", "BQDNvmIAFYyU7KlLOoaAV8TAb2pe5OxcXfr-c9ZnBPIORj3aENjTJdweml7WWLp6UiZCpESBAglj2t2i2alMqSmMC2QDXvUG_sk1hUuuoax7ibsiBQC9DlLdeWzkKLsP_pY0gUmqRSe_BIDBbtCwlSlqbCH2sUkeVKU3_1ITdl6_Yb4sx2dPGXZ5zSB_bSWhkrCzXgx9Pq-JmB_hS3TvDaOQY6m1OsO-8FuAO9cxUPiY9vcocSsCqQoxHSAvKR86h4MYtTV36cVdVPCwxhtaj2tI5ixs-OZ_8C2V8ItkGivejtAYgVCLfmry3pmTEdjV0BBiq5s3V1fb6_p5LnEKz8l8dSUgBAAAAAGUbHYOAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
STATS_IMG_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
STREAM_IMG_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/ab61ba103ac0d30c8a38f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
