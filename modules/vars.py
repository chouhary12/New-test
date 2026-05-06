#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22480303"))
API_HASH = environ.get("API_HASH", "99c931b6c1ae6f8c3c3e87da173fa424")
BOT_TOKEN = environ.get("BOT_TOKEN", "8783249147:AAH35j4k1FjuuXJ_BzGhvtnGqgLDYSaCfU8")

OWNER = int(environ.get("OWNER", "8295147093"))
CREDIT = environ.get("CREDIT", "𝘽𝙊𝙏𝙎")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8295147093').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8295147093').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
