# HashMinner

import os
import math
import json
import time
import shutil
import heroku3
import requests

from pyrogram import filters
from pyrogram import Client as kinu6
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import HEROKU_API_KEY

server = heroku3.from_key(HEROKU_API_KEY)
user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
accountid = server.account().id
headers = {
  'User-Agent': user_agent,
  'Authorization': f'Bearer {Config.HEROKU_API_KEY}',
  'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
}

path = "/accounts/" + accountid + "/actions/get-quota"

request = requests.get("https://api.heroku.com" + path, headers=headers)

if request.status_code == 200:
  result = request.json()
  total_quota = result['account_quota']
  quota_used = result['quota_used']
  quota_left = total_quota - quota_used
  quota_details = f"""
  > __Dyno hours remaining this month__ ;
        - **{hours} hours**  ( {leftperc}% )
        - **Approximately {days} days!**
        """
